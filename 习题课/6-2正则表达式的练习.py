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

# 提取每行中完整的年月入和时间段
s4 = "se2332 1987-10-10 22:44:55   jkasfjakfd 2018-10-20 09:47:20"

content5 = re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", s4)
print(content5)

# 提取电子邮件格式
s5 = "xxxx@gmail.com xxxx@qq.com baidu.com 999.com jkjk@163.com"

content6 = re.findall(r"\w+@\w+.com", s5)
print(content6)

# 把以上合法的电子邮件的地址替换成我自己的电子邮件地址
content7 = re.sub(r"\w+@\w+.com", "athany@qq.com", str(content6))
print(content7)

# 使用正则提取字符串中的单词
s6 = "i love you not because who 233 of 890sdx not"
content8 = re.findall(r"\b[a-zA-Z]+\b", s6)
print(content8)

# 以下两个关于match和search的正则表达式是等价的
content9 = re.match(r"\b[a-zA-Z]+\b", s6)
content10 = re.search(r"^\b[a-zA-Z]+\b", s6)
print(content9.group())
print(content10.group())
