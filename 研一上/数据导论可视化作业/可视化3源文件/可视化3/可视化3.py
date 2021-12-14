#-*- codeing = utf-8 -*-
#@Time :2021/11/11 19:20
#@Author ：Damon老否
#@File : 可视化3.py
#@Software :PyCharm

import jieba        #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud         #词云
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算
import sqlite3                          #数据库

#打开准备好的txt文件，去空格和空行
text = open('../dataset.txt',encoding="utf-8").read().strip(' ').replace("\n", "")
#测试一下
#print(text)

#分词
cut = jieba.cut(text)
string = ' '.join(cut)
#测试看看分好出来的词组
print(string)


#导入图片
img = Image.open(r'.\img\tree.jpg')   #打开遮罩图片
img_array = np.array(img)   #将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc"    #字体所在位置：C:\Windows\Fonts
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')     #是否显示坐标轴

#plt.show()    #显示生成的词云图片

#输出词云图片到文件
plt.savefig(r'.\img\word5.jpg',dpi=1000)