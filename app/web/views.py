# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-14 15:22 
@mail: axingfly@gmail.com

Less is more.
"""

from app.web import web
import app.libs.utils as utils
from flask import request, jsonify


@web.route('/api/ins', methods=['POST'])
def get_ins_urls():
    request_json = request.get_json(silent=True)
    if not request_json:
        return res(400, None, '请传入URL')
    url = request_json.get('url')
    if not url:
        return res(400, None, '参数请求错误')
    if utils.r2(url):
        ins = utils.Ins(url)
        try:
            ins_dict = ins.get_ins_url()
        except:
            return res(500, None, 'Boom💣')
        if not ins_dict:
            return res(404, None, '请求无效')
        return res(200, ins_dict, '请求成功')
    else:
        return res(400, None, '链接🔗错误')


def res(code, data, message):
    return jsonify(code=code, data=data, message=message)
