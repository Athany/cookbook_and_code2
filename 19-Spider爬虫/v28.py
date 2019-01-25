#只找第一个
# find
# name=None, 便签名
#attrs={} ,属性名
# 只找第一个标签
print(soup.find('p'))
# 通过类名来查找节点
print(soup.find('p',attrs={'class':"story"}))
print(soup.find('p',class_="story"))
# 通过id来查找节点
print(soup.find('p',id="story"))
