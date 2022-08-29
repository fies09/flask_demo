#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2022/8/24 22:07
# @Author     : fany
# @Project    : PyCharm
# @File       : databases.py
# @description: 创建数据库
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:fy961009@127.0.0.1:3306/test1'

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + "/Users/fan/Desktop/project/flask_demo/schema/first.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "jjjsks"

db = SQLAlchemy(app)  # 实例化的数据库

if __name__ == '__main__':
    db.create_all()