# css选择器
# 查找id为story下的a(子孙节点)
print(soup.select("#story a"))
# 查找id为story下的子节点下的a(子节点)
print(soup.select("#story > i > a"))
