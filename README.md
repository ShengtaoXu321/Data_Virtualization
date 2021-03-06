# 说明
这是学习bilibili的李巍老师的数可视化代码整理

# 数据可视化
* Flask入门
* Echarts应用
* WordCloud应用
* 项目说明

## 1. Flask入门

### 1.1 关于Flask
* 了解框架

  Flask作为Web框架，它的作用主要是为了开发Web应用程序。那么我们首先来了解下Web应用程序。Web框架：我们只需要知道--请求是什么？响应是什么？--而不需要关注如何去访问的，以及访问了是如何解析的。

  一切从客户端发起请求开始。
  
  * 所有Flask程序都必须创建一个程序实例。
  
  * 当客户端想要获取资源时， 一般会通过浏览器发起HTTP请求
  
  * 此时， Web服务器使用一种名为WEB服务器网关接口的WSGI(Web Server Gateway Interface)协议， 把来自客户端的请求都交给Flask程序实例。
  
  * Flask使用Werkzeug来做路由分发（URL请求和视图函数之间的对应关系）。根据每个URL请求，找到具体的 视图函数。

  * 在Flask程序中，路由一般是通过程序实例的装饰器实现。通过调用视图函数，获取到数据以后，把数据传入HTML模板文件中，模板引擎负责渲染HTTP响应数据，然后由Flask返回响应数据给浏览器， 最后浏览器显示返回的结果。

* 为什么要用Web框架？

  Web网站发展至今，特别是服务器端，涉及到的知识、内容，非常广泛。如果采用成熟、稳健的框架，那么一些基础的工作，比如：网络操作、数据库非访问、会话层的管理等都可以让框架来处理；可以将重心放在：具体的业务逻辑上面。


* Flask框架的诞生：

  Flask诞生于2010年， 是Armin ronacher用Python语言基于Werkzeug工具箱编写的轻量级Web开发框架。它主要面向需求简单的小应用。

  Flask本身就相当于一个内核，其他几乎所有功能都要用到扩展（邮件扩展：Flask-Mail，用户认证：Flask-Login），都需要用到第三方的扩展来实现。比如可以用Flask-extension加入ORM、窗体验证工具、文件上传、身份验证等。Flask没有默认使用的数据库，你可以选择MySQL，也可以用NoSqL。其WSGI工具箱采用Werkzeug（路由模块），模板引擎则使用（Jinja2）。

  **可以说Flask框架的核心就是`Werkzeug`和`Jinja2`。**

  Python最出名的框架要数Django，此外还有Flask、Tornado等框架。

* Flask扩展包：

  * Flask-SQLalchemy：操作数据库

  * Flask-migrate: 管理迁移数据库

  * Flask-Mail： 邮件

  * Flask-WTF: 表单

  * Flask-script：插入脚本

  * Flask-Login： 认证用户状态

  * Flask-RESTful： 开发REST API的工具

  * Flask-Bootstrap: 集成前端Twitter Bootstrap框架

  * Flask-Moment: 本地化日期和时间


### 1.2 Flask的入门

* Hello world 的学习

    代码：
    ```Python
    # 导入Flask类
    from flask import Flask

    # Flask类接收一个参数__name__
    app = Flask(__name__)

    # 装饰器的作用是将路由映射到视图函数index
    @app.route('/')
    def index():
        return 'Hello World'

    # Flask应用程序实例的run方法启动Web服务器
    if __name__ == '__main__':
        app.run()
    ```

## 2. Echarts入门


## 3. WordCloud入门

* WordCoud配置

  WordCloud个参数的含义
  > font_path: string   # 字体路径， 需要展现什么字体就把该字体路径+后缀名写上，如：font_path='黑体.ttf'。
  
  > width: int(default=400)  # 输出的画布宽度， 默认为400像素

  > height: int(default=200)  # 输出的画布高度， 默认为200像素

  > prefer_horizontal: float(default=0.90)  # 词语水平方向排版出现的频率， 默认0.9（所以词语垂直方向排版出现的频率为0.1）

  > mask: nd-array or None(default=None)  # 如果参数为空，则使用二维遮罩绘制词云。如果mask非空，设置的宽高值将被忽略，遮罩形状被mask取代。 除全白（#FFFFFF）的部分将不会被绘制，其余部分会用于绘制词云。 如：bg_pic=imread('读取一张图片.png')，背景图片的画布一定要设置为白色（#FFFFFF），然后显示的形状为不是白色的其他颜色。可以用PS工具将自己显示的形状复制到一个纯白色的画布上再保存，就OK了

  > scale: float(default=1)  # 按照比例进行画布放大，如设置1.5，则长和宽都是原来画布的1.5倍

  > min_font_size: int(defalut=4)  # 显示的最小的字体大小

  > font_step: int(defalut=1)  # 字体步长， 如果步长大于1，会加快运算，但是可能导致结果出现较大的误差

  > max_words: number(default=200)  # 要显示的词的最大个数

  > stopwords：set of strings or None  # 设置需要屏蔽的词， 如果为空，则使用内置的STOPWORDS

  > background_color: color value(defalut='black')  # 背景颜色，如果background_color='white'，背景颜色为白色

  > max_font_size: int or None(defalut=None)  # 显示最大的字体大小

  
