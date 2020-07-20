
from socket import *
import pymysql



db = pymysql.connect(host="localhost",
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8'
                     )

cur = db.cursor()

# 创建udp的套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
udp_socket.bind(("0.0.0.0",8888))

# 接收一个消息
while True:
    # 注意接收到的addr是客户端的地址
    data,addr = udp_socket.recvfrom(1024)
    if data.decode()=="q":
        break
    sql_select_mean = "select mean from words where word=%s;"
    cur.execute(sql_select_mean, data.decode())
    row = cur.fetchone()
    udp_socket.sendto(row[0].encode(), addr)




cur.close()
db.close()
# 关闭套接字
udp_socket.close()

