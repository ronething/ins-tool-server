# ins-tool-server

## Introduction

ins 图片默认是下载不了的。so 解析一下

## Run

```
git clone [repo]
pipenv shell
```

在 `app/config` 目录下新建 `secure.py` 

```python
import os
from dotenv import load_dotenv

load_dotenv()

environ = os.getenv('FLASK_ENV', 'development')

MY_HEADERS = {
    'Referer': 'https://www.instagram.com/',
    'User-Agent': '', 
}

if environ == 'production':

    MY_PROXIES = {}

else:

    MY_PROXIES = {
        'http': 'socks5://host:port',
        'https': 'socks5://host:port'
    }
```

然后

```
pipenv shell
python manage.py
```

## Deployment

### 这次使用的是 Heroku Git 部署

- 首先安装 [heroku cli](https://devcenter.heroku.com/articles/heroku-cli)
- 项目根目录下创建 `Procfile`
- `heroku create your-app`
- `heroku config:set FLASK_ENV=production`
- `git add . && git commit -m "xxx" && git push heroku master`
- 等待构建完成,访问网址即可

## Demo Site

- [ins](http://ins.ronething.com)

## Change Log

- Sun Apr 14 22:02:50 first version

## Acknowledgement

- [you-get](https://github.com/soimort/you-get)
