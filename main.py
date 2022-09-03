from tkinter import ttk
from tkinter import *
import pymysql

Locations=[];
# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="123456", database="cvpr", charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM 财经  WHERE channelName = '财经'"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        age1 = row[1]
        # 打印结果
        Locations.append(age1)
except:
    print("Error: unable to fetch data")
    db.close()
    db = pymysql.connect(host="localhost", user="root", password="123456", database="cvpr", charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
sql = "SELECT * FROM 房产  WHERE channelName = '房产'"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        age2 = row[2]
        # 打印结果
        Locations.append(age2)
except:
    print("Error: unable to fetch data")
# 关闭数据库连接
db.close()
# 初始化窗口window
window = Tk()
window.title('新闻展示')
window.geometry('600x600')

# 声明一个Treeview表,参数为parent
tree = ttk.Treeview(window,show="tree")

# 此处为布局，fill字段为填充方向，可以选择X或者Y或者两者都BOTH，expand字段为布尔类型，对应fill是否填充
tree.pack(fill=BOTH, expand=YES)

# insert(parent,index,iid=None,**kw)
# insert 方法是向Treeview中添加结点，返回值为插入的item
# 参数说明：parent为父节点, ''空串，代表根节点
# index为第几个结点，通常都是用0 或者 'end' 来放置结点到第一个或者最后一个位置
# iid可以显示确定也可以默认
# 关键字字段可以有text属性，用于前端显示文本
# 可以有vlaue属性, 这个字段在树型结构中可以不定义，应该是用于判断节点等价的（理解为hash）
# 可以有open属性，这个字段代表节点默认打开还是关闭，bool型，缺省值为False
item = tree.insert('',0,text='新闻',open=True)
item1 = tree.insert(item,0,text='财经（8597）',value='财经')
item2 = tree.insert(item,0,text='房产（200）' ,value='房产')
# item3 = tree.insert(item,0,text='体育（1200）' ,value='体育')
# item4 = tree.insert(item,0,text='军事（158）' ,value='军事')
# item5 = tree.insert(item,0,text='娱乐（1200）' ,value='娱乐')
# item6 = tree.insert(item,0,text='教育（500）' ,value='教育')
# item7 = tree.insert(item,0,text='汽车（647）' ,value='汽车')
# item8 = tree.insert(item,0,text='游戏（1300）' ,value='游戏')
# item9 = tree.insert(item,0,text='科技（830）' ,value='科技')
count=2;
for age1 in Locations:
    count=count+1;
    Name = item+str(count);
    Name = tree.insert(item1,0,text=age1,value=age2)
count = 2;
for age2 in Locations:
    count = count + 1;
    Name = item + str(count);
    Name = tree.insert(item2, 0, text=age2, value=age2)
    # Name = tree.insert(item3, 0, text=x, value=x)
    # Name = tree.insert(item4, 0, text=x, value=x)
    # Name = tree.insert(item5, 0, text=x, value=x)
    # Name = tree.insert(item6, 0, text=x, value=x)
    # Name = tree.insert(item7, 0, text=x, value=x)
    # Name = tree.insert(item8, 0, text=x, value=x)
    # Name = tree.insert(item9, 0, text=x, value=x)
# 显示窗口
window.mainloop()

