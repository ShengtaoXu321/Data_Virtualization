# =========================================Flask入门上================================================
'''
from flask import Flask, render_template    # render_template是渲染模板

# 对象实例化
app = Flask(__name__)

# =====================================================================================

# 路由解析，通过用户访问的路径，匹配相应的函数
# 可以匹配不同的路由
@app.route('/user/<int:id>')
def index(id):
    return f'Hello World {id}号的会员'

# 访问路径修改
@app.route('/index')    # 访问路径修改
def index1():
    return '你好！'


# 含参数访问： 通过访问路径， 获取用户的字符串参数
@app.route('/user/<name>')
def index2(name):
    return f'Hello World {name}'


# 含参数访问： 通过访问路径， 获取用户的整型参数
@app.route('/user/<int:id>')
def index3(id):
    return f'Hello World {id}'


# 含参数访问： 通过访问路径， 获取用户的float参数
@app.route('/user/<float:id>')
def index4(id):
    return f'Hello World {id}'



# 使用render_template进行渲染   --  展示出想要的HTML文件
# 返回给用户选然后的网页文件
app.route('/test')
def index5():
    return render_template('index.html')    # 返回渲染一个index的html文件   Jinja2实现


# =====================================================================================================
# 调用run
if __name__ == '__main__':
    app.run(debug=True)

# *****总结：
#   路由路径不能重复，用户通过唯一路径访问特定的函数
'''




# ===============================Flask入门下===================================================================
# 导入模块
from flask import Flask, render_template, request
import datetime 

# 对象实例化
app = Flask(__name__)


# 路由解析

# 返回给用户渲染后的网页
@app.route('/')
def index():
    return render_template('index.html')


# 向页面传递一个变量
@app.route('/var')
def index1():
    time = datetime.date.today()                  # 普通变量
    name = ['小王', '小赵', '小张']                # 列表类型
    task = {'任务': '打扫卫生', '时间': '3小时'}    # 字典类型
    return render_template('index.html', var = time, list = name, task = task)    # 逗号后面传递变量,前一个变量是HTML的，后一个是Py的


# 表单提交
@app.route('/test/register')
def register():
    return render_template('test/register.html')     # 上面那个是访问路径，这个是当前文件结构


# 接收表单提交的路由，需要指定methods为post
@app.route('/result', methods=['POST', 'GET'])
def result(): 
    if request.method == 'POST':
        result = request.form  
        return render_template('test/result.html', result=result)     # 上面那个是访问路径，这个是当前文件结构



# 调用run
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000, debug=True)