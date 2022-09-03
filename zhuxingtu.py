# -*- coding:utf-8 -*-
# 申明编码格式为utf-8

import matplotlib as mpl
import matplotlib.pyplot as plt
from labels.cli import labels

mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 指定字体为SimHei，用于显示中文，如果Ariel,中文会乱码
mpl.rcParams["axes.unicode_minus"] = False
# 用来正常显示负号

x = [1,2,3,4,5,6,7,8,9]
y = [30,11,42,53,81,98,72,25,68]
# y1= [45,23,44,67,88,89,65,75]
#数据
labels=["体育","军事","娱乐","房产","教育","汽车","游戏","科技","财经"]
#定义柱子的标签
plt.bar(x,y,align="center",color="b",tick_label=labels,hatch=" ",ec='gray')
#绘制纵向柱状图,hatch定义柱图的斜纹填充，省略该参数表示默认不填充。
# plt.bar(x,y1,align="center",color="g",tick_label=labels,hatch=" ",ec='gray',bottom=y)
# 绘制纵向柱状图,hatch定义柱图的斜纹填充，省略该参数表示默认不填充。

# bar柱图函数还有以下参数：
# 颜色：color,可以取具体颜色如red(简写为r),也可以用rgb让每条柱子采用不同颜色。
# 描边：edgecolor（ec）：边缘颜色；linestyle（ls）：边缘样式；linewidth（lw）：边缘粗细
# 填充：hatch，取值：/,|,-,+,x,o,O,.,*
# 位置标志：tick_label

plt.xlabel(u"样品编号")
plt.ylabel(u"库伦效率/%")

plt.show()