# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-14 13:21 
@mail: axingfly@gmail.com

Less is more.
"""

import os
from dotenv import load_dotenv
import logging

load_dotenv()

environ = os.getenv('FLASK_ENV', 'development')

PORT = 7000

if environ == 'production':

    DEBUG = False

    HOST = '0.0.0.0'

    logging.basicConfig(level=logging.ERROR)

else:

    DEBUG = True

    HOST = '127.0.0.1'

    logging.basicConfig(level=logging.DEBUG)
