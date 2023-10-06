import socket
import sys
import select


# 在TCP连接中recv和send的个数可以不一样，以缓冲池的形式接收

def TCP_server():
    sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if len(sys.argv) == 1:
        addr = ('', 2000)
    else:
        addr = (sys.argv[1], 2000)
    sever.bind(addr)
    sever.listen(128)  # 最多建立128个连接

    # 对epoll进行注册文件描述符
    epoll = select.epoll()  # 一个epoll可以并发的监听多个
    client_list = []
    epoll.register(sever.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)  # 监听输入缓冲池的内容
    while True:
        epoll_list = epoll.poll(-1)  # epoll.poll会返回一个监听列表
        for fd, event in epoll_list:
            if fd == sever.fileno():
                new_server, _ = sever.accept()  # accept()返回第一个socket对象，第二个是客户端地址
                print(_)
                for other_client in client_list:
                    other_client.send(f"{_}进入聊天室".encode("utf8"))
                epoll.register(new_server.fileno(),
                               select.EPOLLIN)  # 监听该连接的缓冲池收到的内容
                client_list.append(new_server)
            else:
                for client in client_list:
                    if client.fileno() == fd:
                        message = client.recv(100)  # recv返回字节流信息
                        if message:
                            for other_client in client_list:
                                if other_client != client:
                                    other_client.send(message)
                        else:
                            for other_client in client_list:
                                if other_client != client:
                                    other_client.send("有人离开聊天室".encode("utf8"))
                            client.close()
                            client_list.remove(client)
                            break
    sever.close()


if __name__ == '__main__':
    TCP_server()
