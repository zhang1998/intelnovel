# -*- coding:utf-8 -*-
# wordcount map阶段
""" 1.读取文件file01，将单词依次存入数组。 2.对数组进行排序。 3.将数组中的单词依次写入文件file02。
"""
ss = []
ff = open("./clean_title.txt", "r")
for x in ff.readlines():
    y = x.strip().split(" ")
    for xx in y:
        ss.append(xx)
ff.close()
ss.sort()
gg = open("./word.txt", "w")
for y in ss:
    gg.write(y)
    gg.write('\n')
gg.close()
