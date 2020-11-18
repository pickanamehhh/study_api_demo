#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: re_demo03.py
# @time: 2020/10/11 9:51 上午

#正则 python中的正则操作  从一个大文本中匹配需要的信息
import re

str1 = 'nEWdream'

value = re.match('n\w+a',str1)   # 正则函数默认是区分大小写的  \w+:表示一个或多个字母、数字、下划线

print( value.group() )

value1 = re.search('n\w',str1)  # 匹配字符模版 和match区别：不是从string的开始位置匹配
print( value1.group() )

str2 = '中国1美国2日本3俄罗斯4德国'
value2 = re.split('\d',str2,2) # 匹配字符模版 根据匹配到的字符模版把string进行切割，返回一个列表
print( value2 )

str3 = '中国1美国22日本325俄罗斯4德国'
value3 = re.split('\d+',str3)
print( value3 )

str4 = 'newdreamnawdbenew'
value4 = re.findall('ben\ww',str4) #以string列表形式返回string中pattern的所有非重叠匹配项
print( value4[0] )

#迭代器
str5 = 'newdreamnawdbenew'
# 匹配整个string 返回一个顺序访问每个匹配结果的迭代器
value5 = re.finditer('n\ww',str5) # 以 iterator 迭代器形式返回string中pattern的所有非重叠匹配项
# iterator 迭代器 只能用来遍历操作
for v in value5:
    print( v.group() )

#sub  替换
str6 = "newdream common !"
#group含义
value6 = re.search("(\w+) (\w+)",str6)
print( value6.group(2) )  # 默认值0  默认组 0 表示匹配的内容 ()新组 1 0 1  2

value7 = re.sub("(\w+) (\w+)",r"\2 \1",str6)  # r 表示原生字符串
print( value7 )

value8 = re.sub("(\w+) (\w+)",r"\2 hello",str6)  # r 表示原生字符串
print( value8 )

#subn 替换，比sub增加了指定替换次数 返回的是一个元祖
str7 = "newdream common !"
value9 = re.subn("(\w+) (\w+)",r"\2 \1",str6)  # r 表示原生字符串
print( value9 )





