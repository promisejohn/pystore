# -*- coding:utf-8 -*-
# !/usr/bin/env python
#
# Author: promisejohn
# Email: promise.john@gmail.com
#
# Config for development
#

import os
BASE_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

# sqlite config
DB_FOLDER = os.path.join(BASE_FOLDER,  '.data')
DB_FILE = 'app.db'
DB_FILEPATH = os.path.join(DB_FOLDER, DB_FILE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_FILEPATH

# logging config
LOGGER_FOLDER = os.path.join(BASE_FOLDER,  '.log')
LOGGER_FILE = os.path.join(LOGGER_FOLDER, 'debug.log')
