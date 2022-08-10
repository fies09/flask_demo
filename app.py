from flask import Flask, redirect, request

app = Flask(__name__)


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
    my_json = request.get_json()
    print(my_json)

    return 'good'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
