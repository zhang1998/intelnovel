#!/usr/bin/python
# -*- coding:utf-8 -*-

word_lst = []
word_dict= {}
with open('clean_title.txt') as wf,open("word.txt",'w') as wf2: #打开文件

    for word in wf.readlines():
        word_lst.append(word.split(' ')) #使用逗号进行切分
        for item in word_lst:
             for item2 in item:
                if item2 not in word_dict: #统计数量
                    word_dict[item2] = 1
                else:
                    word_dict[item2] += 1
#key：分词
#value:个数
    for key in word_dict:
        print key,word_dict[key]


        wf2.write(key+' '+str(word_dict[key])+'\n') #写入文档



'''
结果：

最后 4
欧洲幽蓝 1
集美 1
葡萄牙法多 1
工地 1
知道湖光山色 1
神圣 7
欧洲少女瑞士加游 1

根据词汇数量排序查看：

cat word.txt |sort -nr -k 2|more

神圣 7
最后 4
欧洲幽蓝 1
集美 1
葡萄牙法多 1
工地 1
知道湖光山色 1
欧洲少女瑞士加游 1

'''
