#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2022/8/11 16:16
# @Author     : fany
# @Project    : PyCharm
# @File       : msg.py
# @description:
import json


class Msg(object):
    def __init__(self):
        self.msg = {
            'code': 1,
            'status': True,
            'msg': '',
            'data': {

            }
        }

    def fail(self, msg):
        code = 1
        self.msg['status'] = False
        self.msg['code'] = code
        self.msg['msg'] = msg
        return self

    def success(self, result, msg):
        code = 0
        self.msg['code'] = code
        self.msg['data']["result"] = result
        self.msg['msg'] = msg
        return self