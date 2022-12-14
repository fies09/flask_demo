#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2022/8/18 11:09
# @Author     : fany
# @Project    : PyCharm
# @File       : fast_upload.py
# @description: 将文件上传到阿里云服务器模块
import oss2
import random
from datetime import datetime
from werkzeug.utils import secure_filename

from configs import access_key_id, access_key_secret, bucket_name, endpoint, OssHttps

# 上传逻辑说明
def uploader(file, path="uploadfiles/"):
    """
   上传到阿里云的接口 上传网络流
   调用这个方法的时候
   1.from app.oss import upload
   2.upload.upload_file(images,path)
   :param file: 这里是接流文件
   :param path: 这里是上传到oos里面的哪个文件夹,例如：path = "first/"
   :return: 返回的是图片上传后的具体url
   """
    auth = oss2.Auth(access_key_id, access_key_secret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)
    file = rename(file)
    file_path = path + file.filename  # 拼接文件夹跟更改后的文件名

    # # 前一个是文件的路径名字，后一个是文件的数据
    bucket.put_object(file_path, file)
    url = OssHttps + file_path  # 具体外网可访问的路由
    return url

# 文件名处理
def rename(file):
    """
    修改文件名字为 自定义的 不重复的
    :param file:文件数据
    :return:
    """
    filename = secure_filename(file.filename)

    try:
        get_hz = filename.rsplit('.', 1)[1]  # 获取后缀
        random_num = random.randint(0, 100)
        file.filename = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + str(random_num) + "." + get_hz
    except Exception as e:
        print(e)
        file.filename = datetime.now().strftime("%Y%m%d%H%M%S") + filename
    return file