import socket


# 在TCP连接中recv和send的个数可以不一样，以缓冲池的形式接收

def TCP_server():
    sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("192.168.0.103", 2000)
    sever.bind(addr)
    sever.listen(128)  # 最多建立128个连接
    new_server, _ = sever.accept()  # accept()返回第一个socket对象，第二个是客户端地址
    message = new_server.recv(100)  # recv返回字节流信息
    print(message.decode("utf8"))
    new_server.send("how do you do ".encode("utf8"))  # send()内容之需要填入字节流
    new_server.close()
    sever.close()


if __name__ == '__main__':
    TCP_server()
