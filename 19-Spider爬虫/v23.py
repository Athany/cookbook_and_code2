'''
使用参数headers和params
研究返回结果
'''
import requests

# 完整访问url是下面url加上参数构成
url = "http://www.baidu.com/s?"

kw = {
    "wd": "王八蛋"
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，
# 不需要urlencode()
url = "http://www.baidu.com/s?"
response = requests.get(url, params=kw, headers=headers)

# 查看响应内容，response.text 返回的是Unicode格式的数据
print(response.text)

# 查看响应内容，response.content返回的字节流数据
print(response.content)

# 查看完整url地址
print(response.url)

# 查看响应头部字符编码
print(response.encoding)

# 查看响应码
print(response.status_code)
