# -*- coding:utf-8 -*-
# !/usr/bin/env python
#
# Author: promisejohn
# Email: promise.john@gmail.com
#
# 包含应用全局对象
#

from flask import Flask
import os
import logging
from logging import Formatter
from logging.handlers import RotatingFileHandler
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.marshmallow import Marshmallow
from flask.ext.restful import Api

# flask app
app = Flask(__name__)

# 从根目录的config.py中加载配置项
app.config.from_object('config.dev')


# 初始化根目录临时文件夹: .data, .log
if not os.path.exists(app.config['LOGGER_FOLDER']):
    os.mkdir(app.config['LOGGER_FOLDER'])
if not os.path.exists(app.config['DB_FOLDER']):
    os.mkdir(app.config['DB_FOLDER'])


# 日志配置
handler = RotatingFileHandler(app.config['LOGGER_FILE'],
                              maxBytes=102400,
                              backupCount=1)
handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


# 数据库ORM配置
db = SQLAlchemy(app)

# 对象序列化配置
ma = Marshmallow(app)

# Restful API配置
api = Api(app)
