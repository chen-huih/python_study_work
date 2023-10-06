import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('192.168.0.103', 2000)
s.bind(addr)
temp = s.recvfrom(100)  # 返回两个元素，第一个为信息，第二个是发送方的地址，内部参数大小字节要大于收到的大小
print(temp[0].decode('utf8'))
s.sendto('你也好！！'.encode('utf8'), temp[1])
s.close()
