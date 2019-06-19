import requests

baseurl = 'https://fanyi.baidu.com/sug'

# 存放用来模拟form的数据一定是dict格式
data = {
    # girl是翻译输入的英文内容，应该是由用户输入input，此处使用硬编码
    'kw': 'girl'
}

headers = {
    # 因为使用post，至少应该包含content-length 字段
    'Content-Length': str(len(data))
}

# 有了headers，data，url，就可以尝试发出请求了
rsp = requests.post(baseurl, data=data,  headers=headers)

print(rsp.text)
print(rsp.json())
