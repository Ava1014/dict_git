"""
udp_client.py  客户端
"""
from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)

# 创建UDP套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 客户端不绑定地址，因为无法确定端口是否与其他程序重复

print("输入q退出")
# 发数据
while True:
    msg = input("请输入单词：")
    udp_socket.sendto(msg.encode(),ADDR)
    if msg=="q":
        break
    data, addr = udp_socket.recvfrom(1024)
    print("释义：",data.decode())

udp_socket.close()