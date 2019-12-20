#!/usr/bin/env python
# -*- coding:utf-8 -*-
#读写文件
# w清空写入 ，a 向文件末尾追加内容
f=open("D:\\softwaredata\\python\\1911a\\test.txt",'w',encoding="utf-8")
f.write("hello,word!")
f.writelines(["阿斯顿撒旦\n""4565\n","das\n"])
f.writelines({"54151","51","156"})
f.close()

#读取内容
f=open("D:\\softwaredata\\python\\1911a\\test.txt",'r',encoding="utf-8")
# c=f.read() #读取
c=f.readline() #按行读取 ，一次读取一行
c=f.readline() #按行读取 ，一次读取一行
c=f.readline() #按行读取 ，一次读取一行
#可以指定读取某几行的内容
#c=f.readlines() #读取并存入
print(c)
f.close()


# with open("test.txt",'r',encoding="utf-8")as f:
#     c=f.read()
#     print(c)
# 项目层级
# 项目->包(package) ->模块(module)->类(class) ->方法(function)、变量(attribute)