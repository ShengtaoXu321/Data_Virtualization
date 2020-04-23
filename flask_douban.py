from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def home():
    # return render_template('index.html')
    return index()

@app.route('/movie')
def movie():
    datalist = []
    # 连接数据库
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()
    sql = 'select * from movie250'
    data = cur.execute(sql)
    # 将查询到数据保存到列表
    for i in data:
        datalist.append(i)  # 循环遍历保存
    cur.close()
    conn.close()

    return render_template('movie.html', movies = datalist)

@app.route('/score')
def score():
    score = []  # 评分
    num = []    # 每个评分所统计出的电影数量
    # 连接数据库
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()
    sql = 'select score,count(score) from movie250 group by score'         # 查询分数和人数
    data = cur.execute(sql)
    # 将查询到数据保存到列表
    for i in data:
        score.append(str(i[0]))
        num.append(i[1])
        
    cur.close()
    conn.close()

    return render_template('score.html', score = score, num = num)


@app.route('/word')
def word():
    return render_template('word.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(debug=True)