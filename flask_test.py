from flask import Flask
app = Flask(__name__)


# 初代路由代码
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# 包含动态路由
@app.route('/user/<name>')
def user(name):
    # return '<h1>Hello, %s!</h1>' %name
    return f'<h1>Hello {name}!</h1>'



# 启动服务器
if __name__ == '__main__':
    app.run(debug=True)