from flask import Flask, redirect, request, jsonify, session
from configs import access_key_id, access_key_secret, endpoint, bucket_name
from configs.log import logger
from werkzeug.utils import secure_filename
import traceback
import random
import datetime
import os
from utils import uploader, tx_uploader
# 获取当前文件的绝对路径
basedir  = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = 'sadsadasfafasfasfsafa'

class API(object):
    def __init__(self):

        routes = [
            # 主页接口
            {'r': '/', 'm': ['GET'], 'f': self.hello_world},
            {'r': '/bilibili', 'm': ['GET'], 'f': self.bilibili},
            {'r': '/hey/<username>', 'm': ['GET'], 'f': self.username},
            {'r': '/my/<float:number>', 'm': ['GET'], 'f': self.number},
            {'r': '/test/my/frist', 'm': ['POST'], 'f': self.first_post},
            {'r': '/login', 'm': ['POST'], 'f': self.login},
            {'r': '/session', 'm': ['GET'], 'f': self.session},
            {'r': '/logout', 'm': ['GET'], 'f': self.logout},
            {'r': '/upload', 'm': ['POST'], 'f': self.upload},
            {'r': '/uploader', 'm': ['POST'], 'f': self.uploader},
            {'r': '/tx_uploader', 'm': ['POST'], 'f': self.tx_uploader},
        ]
        for route in routes:
            self.addroute(route)

    @staticmethod
    def addroute(route):
        app.add_url_rule(route['r'], view_func=route['f'], methods=route['m'])

    def hello_world(self):  # put application's code here
        return 'Hello 音宫'

    def bilibili(self):  # put application's code here
        return redirect("https://www.bilibili.com")

    def username(self, username):  # put application's code here
        return '我是 %s' % (username + username)

    def number(self, number):  # put application's code here
        return '我的数据 %s' % (number + number)

    def first_post(self):
        try:
            my_json = request.get_json()
            print(my_json)
            get_name = my_json['name']
            get_age = my_json['age']
            if not all([get_name,get_age]):
                return jsonify(msg = "缺少参数")
            get_age += 10
            return jsonify(name=get_name, age=get_age)
        except Exception as e:
            print(e)
            return jsonify(msg="出错了,请看是否正确访问")

    #登录
    def login(self):
        '''
        账号: username  admin
        密码: password  admin123456
        :return:
        '''
        get_date = request.get_json()
        username = get_date.get('username')
        password = get_date.get('password')

        if not all([username, password]):
            return jsonify(msg = '参数不全')

        if username == 'admin' and password == 'admin123456':
            # 如果验证通过 登录信息保存在session中
            session['username'] = username
            return jsonify(statusCode=200, msg='登录成功')
        else:
            return jsonify(statusCode=500, msg='账号或密码错误')

    #登录状态
    def session(self):
        username = session.get('username')
        if username is not None:
            #操作逻辑,对数据库数据进行处理之类的
            return jsonify(username=username)
        else:
            return jsonify(msg='出错了,没登录')


    #退出
    def logout(self):
        session.clear()
        return jsonify(msg='成功退出登录')

    # # 文件上传
    # def upload(self):
    #     try:
    #         file1 = request.files.getlist('file1')
    #         file2 = request.files.getlist('file2')
    #         if len(file1) != len(file2):
    #             logger.info('文件数量不一致,请重新输入')
    #         else:
    #             upload1_path = []
    #             for filename1 in file1:
    #                 filename_1 = secure_filename(filename1.filename)
    #                 file_name1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_1" + "." + \
    #                              filename_1.rsplit('.', 1)[1]
    #                 file_name2 = file_name1.replace("_1", "-2")
    #                 file_path = basedir + "/images/"
    #                 # 判断文件夹是否存在 不存在则创建
    #                 if not os.path.exists(file_path):
    #                     os.makedirs(file_path, 755)
    #                 file1_path = file_path + '/image1/' + file_name1
    #                 upload1_path.append(file1_path)
    #                 # 将文件保存到目标文件夹
    #                 filename1.save(file1_path)
    #                 upload2_path = []
    #                 for filename2 in file2:
    #                     file2_path = file_path + '/image2/' + file_name2
    #                     upload2_path.append(file2_path)
    #                     filename2.save(file2_path)
    #             logger.info("文件上传成功")
    #         return jsonify({"statusCode": 200, "msg": "success"})
    #     except Exception as e:
    #         logger.error(f"文件上传异常异常:{traceback.format_exc()}行数:{e.__traceback__.tb_lineno}")
    #         return jsonify({"statusCode": 500, "msg": "fail"})


    # 图片上传到本地服务器
    def upload(self):
        try:
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

            file_path = basedir + '/static/file/'
            # 判断文件夹是否存在, 不存在则创建
            if not os.path.exists(file_path):
                os.makedirs(file_path, 755)
            f.save(file_path + filename)
            logger.info("已将文件成功保存到本地服务器")
            # 可以配置成对应的外网访问链接,
            my_host = "http://127.0.0.1:8088"
            new_path_file = my_host + '/static/file/' + filename
            logger.info("前端可访问的链接为:" + new_path_file)
            return jsonify({"statusCode": 200, "msg": '文件上传到服务器成功', 'url': new_path_file})
        except Exception as e:
            logger.error(f"文件保存到服务器异常:{traceback.format_exc()}行数:{e.__traceback__.tb_lineno}")
            return jsonify({"statusCode": 500, "msg": "文件上传失败"})

    # 上传文件到阿里云服务器
    def uploader(self):
        file = request.files.get("file")
        # 保存图片到对象存储
        try:
            file_url = uploader.uploader(file)
            logger.info("上传文件到阿里云成功")
            return jsonify({"statusCode": 200, "msg": "保存图片数据成功", "data": file_url})
        except Exception as e:
            logger.error(f"图片上传失败:{traceback.format_exc()}行数:{e.__traceback__.tb_lineno}")
            return jsonify({"statusCode": 500, "msg": "文件上传失败"})

    # 上传文件到腾讯云
    def tx_uploader(self):
        file = request.files.get("file")
        # 保存图片到对象存储
        try:
            uploader.uploader(file)
            logger.info("上传文件到腾讯云成功")
            return jsonify({"statusCode": 200, "msg": "保存图片数据成功"})
        except Exception as e:
            logger.error(f"图片上传失败:{traceback.format_exc()}行数:{e.__traceback__.tb_lineno}")
            return jsonify({"statusCode": 500, "msg": "文件上传失败"})

    @staticmethod
    def start():
        app.run(host='0.0.0.0', port=8088, debug=False)

server = API()
logger.info('[+] AGX API is running [%s]' % datetime.datetime.now())

if __name__ == '__main__':
    server.start()


