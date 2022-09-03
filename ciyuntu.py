import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 读取Text文本
data = open('测试.txt', "r", encoding="utf-8").read()
# 将文本已词语的方式分割 分割后赋值给Word
# ut_all=True 是全模式 cut_all=False 是精确模式 默认是精确模式
cutData = jieba.cut(data, cut_all=False)
# 以空格分开词语
word = " ".join(cutData)

# 背景图
mask = np.array(Image.open("马.jpg"))

# '''
# WordCloud()可选的参数
# font_path：可用于指定字体路径，包括otf和ttf
# width：词云的宽度，默认为400
# height：词云的高度，默认为200
# mask：蒙版，可用于定制词云的形状
# min_font_size：最小字号，默认为4
# max_font_size：最大字号，默认为词云的高度
# max_words：词的最大数量，默认为200
# stopwords：将被忽略的停用词，如果不指定则使用默认的停用词词库
# background_color：背景颜色，默认为black
# mode：默认为RGB模式，如果为RGBA模式且background_color设为None，则背景将透明
# '''

wc = WordCloud(mask=mask, font_path='HYXiXingKaiW.ttf', mode='RGBA', background_color='black').generate(word)

# 下面代码表示显示图片
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存图片
wc.to_file('D:\java 王建民\2021下\11.25极限测试\cloud_img.png')