# -*- coding:utf-8 -*-
import shutil
def alter(file,old_str,new_str):
    with open(file, "r") as f1,open("%s.bak" % file, "w") as f2:
        for line in f1:
            if old_str in line:
                line = line.replace(old_str, new_str)
            f2.write(line)



#一个进行行替换的函数

old={"百度":"谷歌"}
shutil.copyfile("./test.txt","fileformanage.txt")
for key in old:
    alter("./fileformanage.txt",key,old[key])
