# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-14 15:23 
@mail: axingfly@gmail.com

Less is more.
"""

import requests
import re
import json
from flask import current_app
import logging


def r1(pattern, text):
    m = re.search(pattern, text)
    if m:
        return m.group(1)


def r2(text):
    """是否匹配 ins 链接"""
    m = re.match(r'https://www.instagram.com/p/[^/]+', text)
    if m:
        return True
    else:
        return False


class Ins(object):

    def __init__(self, url):
        self.url = r1(r'([^?]*)', url)
        self.headers = current_app.config['MY_HEADERS']
        self.proxies = current_app.config['MY_PROXIES']

    def get_html(self):
        try:
            response = requests.get(self.url, headers=self.headers, proxies=self.proxies)
            if response.status_code == 200:
                return response.text
            else:
                logging.debug('请求网页源代码错误, 错误状态码：{}'.format(response.status_code))
                return None
        except Exception as e:
            print(e)
            return None

    def get_ins_url(self):
        urls = []

        html = self.get_html()
        if not html:
            return None

        vid = r1(r'instagram.com/p/([^/]+)', self.url)
        description = r1(r'<meta property="og:title" content="([^"]*)"', html)
        title = "{} [{}]".format(description.replace("\n", " "), vid)
        stream = r1(r'<meta property="og:video" content="([^"]*)"', html)

        if stream:
            urls.append(stream)
        else:
            data = re.search(r'window\._sharedData\s*=\s*(.*);</script>', html)
            info = json.loads(data.group(1))

            if 'edge_sidecar_to_children' in info['entry_data']['PostPage'][0]['graphql']['shortcode_media']:
                edges = info['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children'][
                    'edges']
                for edge in edges:
                    image_url = edge['node']['display_url']
                    if 'video_url' in edge['node']:
                        image_url = edge['node']['video_url']
                    urls.append(image_url)

            else:
                image_url = info['entry_data']['PostPage'][0]['graphql']['shortcode_media']['display_url']
                if 'video_url' in info['entry_data']['PostPage'][0]['graphql']['shortcode_media']:
                    image_url = info['entry_data']['PostPage'][0]['graphql']['shortcode_media']['video_url']
                urls.append(image_url)

        return dict(title=title, urls=urls)


def main():
    url = 'https://www.instagram.com/p/BwMJuDVgH7S/?utm_source=ig_web_copy_link'
    ins = Ins(url)
    ins_dict = ins.get_ins_url()
    print("====")
    print(ins_dict)
    print("====")
    pass


if __name__ == '__main__':
    main()
