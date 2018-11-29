# -*- coding: utf-8 -*-
import sys
import jieba
from os import path
import sys

reload(sys)
sys.setdefaultencoding('utf8')
d = path.dirname(__file__)
stopwords_path = './stopwords.txt' # 停用词词表

text_path = './test.txt' #设置要分析的文本路径
text = open(path.join(d, text_path)).read()

def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open(stopwords_path)
    try:
        f_stop_text = f_stop.read( )
        f_stop_text=unicode(f_stop_text,'utf-8')
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)

text1 = jiebaclearText(text)
print text1
f=open('clean_title.txt','w')
f.write(text1)
