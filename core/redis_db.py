#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2022/8/24 20:34
# @Author     : fany
# @Project    : PyCharm
# @File       : redis_db.py
# @description:
# -*- coding: utf-8 -*-
import redis

from configs import db_redis

pool = redis.ConnectionPool(**db_redis)
RedisClient = redis.Redis(connection_pool=pool)

__all__ = ['RedisClient']