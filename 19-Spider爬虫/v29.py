#查找全部
# find_all
'''
 参数：name=None, attrs={}, recursive=True,
 text=None,limit=None, **kwargs
'''
# 查找所有符合的标签，返回一个列表
print(soup.find_all('p'))
# 限制输出
print(soup.find_all('a',limit=2))
# 使用正则
print(soup.find_all(re.compile('^p')))
print(soup.find_all(text=re.compile("^L")))
