import random

from flask import Flask, redirect, request, jsonify, session
from configs.log import logger
from werkzeug.utils import secure_filename
import datetime
import os
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
            session['username']  = username
            return jsonify(msg='登录成功')
        else:
            return jsonify(msg='账号或密码错误')

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

    #图片上传接口
    def upload(self):
        f = request.files.get('file')
        # 获取安全的文件名, 正常的文件名
        filename = secure_filename(f.filename)
        # 生成随机数
        random_num = random.randint(0, 100)
        # 文件后缀
        # file_type = f.filename.strip('.', 1)[1]
        # 把文件重命名
        filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '_' + str(random_num) + '.' + filename.rsplit('.', 1)[1]
        if not os.path.exists(filename):
            os.makedirs(filename, 755)
        file_path = basedir + '/data_pkg/' + filename
        f.save(file_path)

        # 可以配置成对应的外网访问链接,
        my_host = "http://127.0.0.1:5000"
        new_path_file = my_host + filename
        data = {"msg": "sussess", "url": new_path_file}

        payload = jsonify(data)
        return payload, 200
        pass

    @staticmethod
    def start():
        app.run(host='0.0.0.0', port=8088, debug=False)

server = API()
logger.info('[+] AGX API is running [%s]' % datetime.datetime.now())

if __name__ == '__main__':
    server.start()


