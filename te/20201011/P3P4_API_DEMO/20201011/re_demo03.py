#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: re_demo03.py
# @time: 2020/10/11 9:51 上午

#正则 python中的正则操作  从一个大文本中匹配需要的信息
import re

str1 = '12#45newdream6789'

# 方式一：
# 先创建pattern对象
pattern = re.compile('12\D45')  #\d 0--9

result1 = re.match(pattern,str1)    # match()匹配以指定的模版开头的字符串

print( result1.group() )

#方式二：
result2 = re.match('12\D45',str1)
print( result2.group() )

#方法三：
str3 = 'NeWdream'
result3 = re.match('new',str3,flags=re.IGNORECASE)
print( result3.group() )
