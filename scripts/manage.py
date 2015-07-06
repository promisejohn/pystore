# -*- coding:utf-8 -*-
# !/usr/bin/env python
#
# Author: promisejohn
# Email: promise.john@gmail.com
#
# Manage.py实现应用管理工具
#

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

# Run python scripts/manage.py cmd
import sys
sys.path.append('.')

from prony import app, db # flake8: noqa

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


# 创建数据库结构
@manager.command
def initdb():
    db.create_all()
    print 'Database inited, location: ' + app.config['SQLALCHEMY_DATABASE_URI']


# 清除数据
@manager.command
def dropdb():
    db.drop_all()
    print 'Database droped.'


# 实现manage.py shell的自动导入对象
def _make_context():
    return dict(app=app, db=db)
manager.add_command("shell", Shell(make_context=_make_context))


if __name__ == '__main__':
    manager.run()
