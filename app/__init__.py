# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-14 13:20 
@mail: axingfly@gmail.com

Less is more.
"""

from flask import Flask
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.secure")
    app.config.from_object("app.config.setting")
    register_blueprint(app)
    CORS(app)

    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)