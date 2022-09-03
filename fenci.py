import cur as cur
import item as item
import jieba
import pandas as pd
import re
from collections import Counter
import MySQLdb
import MySQLdb.cursors
conn = MySQLdb.Connect(host = '127.0.0.1',
                       port = 3306,
                       user = 'root',
                       passwd = '123456',
                       db = 'cvpr',
                       charset='utf8')


cut_words=""
cur = conn.cursor()
fileNameStr1 = r'D:\java 王建民\2021下\11.25极限测试\总数据.csv'
for line in open(fileNameStr1,encoding='utf-8'):
    line.strip('\n')
    line = re.sub("[A-Za-z0-9\：\·\—\，\。\“ \”]", "", line)
    seg_list=jieba.cut(line,cut_all=False)
    cut_words+=(" ".join(seg_list))
all_words=cut_words.split()
print(all_words)
c=Counter()
for x in all_words:
    if len(x)>1 and x != '\r\n':
        c[x] += 1

print('\n词频统计结果：')
for (k,v) in c.most_common():# 输出词频最高的前两个词
    into = "INSERT INTO 总词(keyword,number) VALUES (%s,%s)"
    values = (k, v)
    cur.execute(into, values)
    conn.commit()
    print("%s:%d"%(k,v))

conn.close()