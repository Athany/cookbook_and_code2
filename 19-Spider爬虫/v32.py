import re

# 一下正则分成两个组，以小括号为单位
s = r'([a-z]+) ([a-z]+)'
pattern = re.compile(s,re.I) # s.I表示忽略大小写

m = pattern.match("Hello world wide web")

# group(0)表示返回匹配成功的整个字符串
s0 = m.group(0)
print(s0)

a0 = m.span(0) # 返回匹配成功的整个字符串的跨度
print(a0)

# group(1)表示返回匹配成功的第一个字符串
s1 = m.group(1)
print(s1)

a1 = m.span(1) # 返回匹配成功的第一个字符串的跨度
print(a1)

s = m.groups() #等价于ｍ.group(1),m.group(2)........
print(s)