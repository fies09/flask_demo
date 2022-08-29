import datetime
import os
import random
import traceback
import oss2
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

from configs import access_key_id, access_key_secret, endpoint, bucket_name
# 获取当前文件的绝对路径
from configs.log import logger

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

class API(object):
    def __init__(self):
        routes = [
            # 文件上传接口
            {'r': '/upload', 'm': ['POST'], 'f': self.upload},
        ]
        for route in routes:
            self.addroute(route)

    @staticmethod
    def addroute(route):
        app.add_url_rule(route['r'], view_func=route['f'], methods=route['m'])

    def upload(self):
        # 对本地文件进行处理
        f = request.files.get('file')
        # 获取安全的文件名, 正常的文件名
        filename = secure_filename(f.filename)
        # 生成随机数
        random_num = random.randint(0, 100)
        # 文件后缀
        # file_type = f.filename.strip('.', 1)[1]
        # 把文件重命名
        filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '_' + str(random_num) + '.' + \
                   filename.rsplit('.', 1)[1]
        if not os.path.exists(filename):
            os.makedirs(filename, 755)
        file_path = basedir + '/' + 'data_pkg' + '/' + filename
        f.save(file_path)
        # 可以配置成对应的外网访问链接,
        my_host = "http://0.0.0.0:8088"
        new_path_file = my_host + filename
        logger.info("文件已成功并保存到本地服务器,前端可访问的链接为:" + new_path_file)
        try:
            # 对文件进行上传到服务器处理, 获取Object完整路径
            object_name = 'upload_files' + "/" + filename
            auth = oss2.Auth(access_key_id, access_key_secret)
            # 填写Bucket名称，例如examplebucket。
            bucket = oss2.Bucket(auth, endpoint, bucket_name)
            # 生成上传文件的签名URL，有效时间为60秒
            url = bucket.sign_url('PUT', object_name, 60, slash_safe=True)
            # 使用签名URL上传本地文件
            result = bucket.put_object_with_url_from_file(url, file_path)
            statusCode = result.status
            logger.info(filename + ": 文件已经成功上传")
            return jsonify({"msg": "文件上传成功", "statusCode": statusCode})
        except Exception as e:
            logger.error(f"文件上传失败:{traceback.format_exc()}行数:{e.__traceback__.tb_lineno}")
            return jsonify({"msg": "文件上传失败", "statusCode": 500})

    @staticmethod
    def start():
        app.run(host='0.0.0.0', port=8088, debug=False)

server = API()
logger.info('[+] AGX API is running [%s]' % datetime.datetime.now())

if __name__ == '__main__':
    server.start()


