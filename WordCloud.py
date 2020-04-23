import jieba        # 分词
from matplotlib import pyplot as plt    # 绘图， 数据可视化
from wordcloud import WordCloud         # 词云
from PIL import Image                   # 图片处理
import numpy as np                      # 矩阵运算
import sqlite3                          # 数据库

# 连接数据库    sqlite3
conn = sqlite3.connect('movie.db')
cur = conn.cursor()
sql = 'select instroduction from movie250'
data = cur.execute(sql)
text = ''
for item in data:
    text = text + item[0]
cur.close()
conn.close()

# 分词  jieba
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))


# 绘图 PIL-Image
img = Image.open(r'.\static\assets\img\tree.jpg')   # 打开遮罩图片
img_array = np.array(img)                           # 将遮罩图片转换成数组
wc = WordCloud(                                     # 词云对象封装
    background_color = 'white',                     # 设置输出图片的背景色
    mask = img_array,                                # 要进行遮罩的图片
    font_path = 'msyh.ttc'                          # 设置字体， 系统的字体所在路径： C:\Windows\Fonts
)

wc.generate_from_text(string)


# 绘制图片 pyplot
fig = plt.figure(1)
plt.imshow(wc)      # 按什么方式显示
plt.axis('off')     # 是否显示坐标轴

# plt.show()        # 显示生成的词云图片

plt.savefig(r'.\static\assets\img\word.jpg', dpi=500)