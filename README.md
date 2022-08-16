1,flask目录(api目录结构)

####1. 目录结构描述 
├──  configs               // 配置文件目录
│    ├──  __init__.py        // 数据库连接，api接口，中间件等配置信息
│    ├──  log.py             // log的输出配置文件
├──  core                  // 封装调用方法目录
│    ├──  dict_config.py     // 配置需要编码转换文件
│    ├──  db.py              // 封装mysql数据库连接配置
│    ├──  redis_db.py        // 封装redis数据库连接配置
├──  data_pkg              // 文件存储目录
├──  logs                  // 日志存放目录
├──  schema                // 和mysql数据库交互目录
│    ├──  models.py          // ORM关系映射模板文件
│    ├──  deploy.sh          // 生成models.py文件脚本
├──  test                  // 测试目录
├──  utils                 // 常用配置工具目录
├──  API.py                // API接口主程序

2,返回值返回格式:
'''
python3
方法一:
# 返回成功
from utils.msg import Msg
msg = Msg()
return msg.success(msg='机器人状态信息获取成功', result=data_dict).json()
# 返回失败
return msg.fail(msg='机器人状态信息获取失败').json()
方法二:
# 返回成功
return {"statusCode": 200, 'msg': 'xxx成功'}
# 返回失败
result = {"statusCode": 500, 'msg': 'xxx异常'}
return json.dumps(result)
方法三:
# 返回成功
return json.dumps({"code": 200, "msg": "success！"}, ensure_ascii=False)
# 返回失败
return json.dumps({"code": 500, "msg": "fail！"}, ensure_ascii=False)
''''

3,异常处理格式:
try:
    pass
except Exception as e:
    logger.error(f"xx异常:{traceback.format_exc()}行数:{e.__traceback__.tb_lineno}")

4,项目环境打包方式:
安装第三方模块:
    pip3 install pipreqs
生成配置文件requirements.txt,在项目根目录下执行
    pipreqs ./ --encoding=utf8 --force
参数说明:当要更新配置文件时,"--force"会覆盖之前生成的配置文件

5,flask重定向总结: 
    1,字符串格式
        return ""
    2,response字符串格式
        return response("")
    3,json格式:
        return jsonify(msg="","statusCode" = 200) 	 
        return jsonify(dict_data)
        return json.dumps(dict_data)
    4,页面跳转
        return render_template("文件名")
    5,重定向：实现页面跳转
        return redirect(user_for("函数名"))	# 通过函数名实现页面跳转
        return redirect('/')
        return redirect('url地址')

6, post请求方式传参参数类型
    string: (缺省值)接受任何不包含斜杠的文本
    int: 接受正整数
    float: 接受征服点型
    path: 类似string, 但可以包含斜杠
    uuid: 接受UUID

7, postman
    params: 在url中添加参数,"?"用于区分,"&"用于拼接.  eg: http://www.baidu.com/obj?key1=1&key2=2
    body ---> form_data (传递json类型的参数,可以上传文件,文件操作), k-v的形式传参
    body ---> raw (可以传递不同格式的文件,对应的请求头分别是
                    text: text/plain,
                    javascript: application/javascript,
                    json: application/json,
                    html: application/html,
                    xml: application/xml
                ), 字典形式传参
    binary: 用于二进制文件处理,eg:文件上传

8,请求参数的获取,post参数一般是json格式(bady--raw--json)或者表单格式(bady--from_data)
    ① json格式的参数获取
        get_data = resquest.get_json()
    ② get请求参数获取
         if request.method == "GET":
            Id = request.args.get("id")
         else:
            Id = request.form.get("id")