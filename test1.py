# -*- coding: utf-8 -*-
'''
1、使用jieba先对中文文档进行分词处理

需要处理的clean_data.csv文件内容（三列）

http://you.ctrip.com/travels/1322/1360550.html   地中海邮轮+罗马深度自由行      宅猫行天下
http://you.ctrip.com/travels/1400/1600356.html  柏林&安纳西     老鼠m
'''
import sys



import jieba
import jieba.analyse

wf = open('clean_title.txt','w+')
sys.getdefaultencoding()
for line in open('test.txt'):

    item = line.strip('\n\r').split('\t') #制表格切分
    # print item[1]
    tags = jieba.analyse.extract_tags(item) #jieba分词
    tagsw = ",".join(tags) #逗号连接切分的词
    wf.write(tagsw)

wf.close()
'''
输出的clean_title.txt内容

邮轮,地中海,深度,罗马,自由纳西,柏林签证,步行,三天,批准申根,手把手,签证,申请,如何赞爆,法兰,穿越,葡萄酒,风景,河谷,世界欧洲颜色,一种,国家,一个水族箱,帕劳,七日,上帝奥林匹亚,跑步圣托,
里尼,文明古国,探访,爱琴海,魅力,希腊
'''
