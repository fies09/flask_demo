#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2022/8/17 19:19
# @Author     : fany
# @Project    : PyCharm
# @File       : __init__.py
# @description:
# 阿里云服务器的配置信息
# yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
endpoint = 'https://oss-cn-hangzhou.aliyuncs.com'
# 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
access_key_id = 'LTAI5t71rGoxcCMRoLp3pk1P'
access_key_secret = 'uY5027VZIrZhbANmtYwt9gIboU5tuf'
# 填写Bucket名称，例如examplebucket。
bucket_name = 'ytwl-files'
# $roleName为RAM角色名称。您可以通过登录RAM控制台，单击左侧导航栏的RAM角色管理，在RAM角色名称列表下进行查看。
role_arn = 'acs:ram::1702972152849983:role/dajiang'
# bucker域名
OssHttps = 'https://ytwl-files.oss-cn-hangzhou.aliyuncs.com/'

# 腾讯云配置文件
import os
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

# # 配置信息
# bucket = os.environ.get("COS_bucket") or 'mnp-1300173558'
# secret_id = os.environ.get("TENCENT_APP_ID") or 'xxxx'  # 替换为用户的 secretId
# secret_key = os.environ.get("TENCENT_APP_KEY") or 'xxxx'  # 替换为用户的 secretKey
# region = os.environ.get("COS_region") or 'ap-shanghai'  # 替换为用户的 Region
# token = None  # 使用临时密钥需要传入 Token，默认为空，可不填
# scheme = 'https'  # 指定使用 http/https 协议来访问 COS，默认为 https，可不填


# config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# # 2. 获取客户端对象
# client = CosS3Client(config)

db_mysql = {
    'host': '192.168.1.8',
    'port': '3306',
    'database': "test",
    'user': "root",
    'pwd': "fy1009",
}
db_redis = {
    'host': '192.168.10.100',
    'password': "123",
    'port': 6379,
    'db': 0,
    'max_connections': 5
}
db_rabbit_mq = {
    "host": "192.168.10.100",
    "port": 5672,
    "vhost": "/",
    "user": "admin",
    "passwd": "admin",
    "robot_exchange": "robot",
    "robot_warn": "warn",
    "warn_queue": "alarm",
    "warn_rout_key": "warn_info",

    #:robot，绑定队列taskState，routingKey为taskStatus

    "robot_task": "robot",
    "task_queue": "taskState",
    "task_rout_key": "taskStatus",

    "rout_send_robotStatus": "robotStatus",
    "queue_send_robotStatus": "robotStatus",
    "rout_send_robotTask": "robotTask",
    "queue_send_robotTask": "robotTask",

    "rout_ex": "robot",
    "rout_send_robotVoice": "robotVoice",
    "queue_send_robotVoice": "robotVoice",

    "test_rout_key": "robot_test",
    "test_queue": "robot_test",

    # 1)路由名为:warn，绑定队列 alarm,routingKey 为 warn_info
}

# 1)路由名为:robot，绑定队列send_serverid，routingKey为robotStatus
