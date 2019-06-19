'''
- Client端流程
            1. 建立通信的socket
            2. 发送内容到指定服务器
            3. 接受服务器给定的反馈内容
'''
# socket模块负责socket编程
import socket


def clientFunc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = "I love zhouxiao"

    # 发送的数据必须是bytes
    data = text.encode()

    # 发送
    sock.sendto(data, ("127.0.0.1", 7852))  # 无法发送127.0.0.1时检查是否开启了防火墙，关闭之后美滋滋。

    data, addr = sock.recvfrom(500)

    data = data.decode()
    print(data)


if __name__ == "__main__":
    clientFunc()
