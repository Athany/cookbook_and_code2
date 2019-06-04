#-*- coding:utf-8 -*-
# @Time  ：2019/6/2 22:45
# @Author: Athany
# @File  : 6-2正则表达式的练习.py

import re
# 匹配一行文字中的所有开头的字母


s = "i love you but you don\'t love me"

# \b\w findall

content = re.findall(r'\b\w', s)
print(content)


content1 = re.findall(r'\w\b', s)
print(content1)

# 匹配一行文字中的所有数字开头的内容
s1 = "i 22love 33you 44but 5you don\'t666 7love 99me"
content2 = re.findall(r'\b\d', s1)
print(content2)


# 匹配只含数字和字母的行
s2 = "i love you \n2222kkkk but \ndfefe23 you don\'t love \n23243dd"
content3 = re.findall(r"\w+", s2, re.M)
print(content3)
# 写一个正则表达式，使其能匹配以下字符，"bit","bat","but","hat","hit","hut".

s3 = "'bit', 'bat', 'but', 'hat', 'hit', 'hut'"
content4 = re.findall(r"..t", s3)
print(content4)
