#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2022/8/24 20:35
# @Author     : fany
# @Project    : PyCharm
# @File       : thread_pool.py
# @description:
from concurrent.futures.thread import ThreadPoolExecutor

Pool = ThreadPoolExecutor(max_workers=20)

__all__ = ['Pool']