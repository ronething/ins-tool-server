# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-14 15:22 
@mail: axingfly@gmail.com

Less is more.
"""

from flask import Blueprint

web = Blueprint("web", __name__)

from . import views
