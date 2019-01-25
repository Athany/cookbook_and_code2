
import requests
from urllib import parse
baseurl = 'https://fanyi.baidu.com/sug'


# 存放用来模拟form的数据一定是dict格式
data = {
    # girl是翻译输入的英文内容，应该是由用户输入，此处使用硬编码
    'kw': 'girl'
}
# data = parse.urlencode(data).encode("utf-8")
# print(type(data))
#  我们需要构造一个请求头，请求头部应该至少包含传入的数据的长度
# request要求传入的请求头是一个dict格式

headers = {
    # 因为使用post，至少应该包含content-length 字段
    'Content-Length':str(len(data))
}


# 有了headers，data，url，就可以尝试发出请求了
rsp = requests.post(baseurl, data=data,  headers=headers)

print(rsp.text)
print(rsp.json())