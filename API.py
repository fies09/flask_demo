from flask import Flask, redirect, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'sadsadasfafasfasfsafa'

@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return 'Hello 音宫'

@app.route('/bilibili')
def bilibili():  # put application's code here
    return redirect("https://www.bilibili.com")

@app.route('/hey/<username>')
def username(username):  # put application's code here
    return '我是 %s' % (username + username)

@app.route('/my/<float:number>')
def number(number):  # put application's code here
    return '我的数据 %s' % (number + number)

@app.route('/test/my/frist', methods=['POST'])
def first_post():
    try:
        my_json = request.get_json()
        print(my_json)
        get_name = my_json['name']
        get_age = my_json['age']
        if not all([get_name,get_age]):
            return jsonify(msg = "缺少参数")
        get_age += 10
        return jsonify(name = get_name, age = get_age)
    except Exception as e:
        print(e)
        return jsonify(msg = "出错了,请看是否正确访问")

#登录
@app.route('/login',methods=['POST'])
def login():
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

#登录
@app.route('/session',methods=['GET'])
def login():
    username = session.get('username')
    if username is not None:
        #操作逻辑,对数据库数据进行处理之类的
        return jsonify(username=username)
    else:
        return jsonify(msg='出错了,没登录')


#
@app.route('/logout',methods=['GET'])
def logout():
    session.clear()
    return jsonify(msg='成功退出登录')


if __name__ == '__main__':
    app.run(host='0.0.0.0')


