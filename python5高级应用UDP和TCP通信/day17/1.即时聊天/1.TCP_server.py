import socket
import sys
import select


# 在TCP连接中recv和send的个数可以不一样，以缓冲池的形式接收

def TCP_server():
    sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (sys.argv[1], 2000)
    sever.bind(addr)
    sever.listen(128)  # 最多建立128个连接
    new_server, _ = sever.accept()  # accept()返回第一个socket对象，第二个是客户端地址
    # 对epoll进行注册文件描述符
    epoll = select.epoll()  # 一个epoll可以并发的监听多个
    epoll.register(new_server.fileno(), select.EPOLLIN)  # 监听该连接的缓冲池收到的内容
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)  # 监听输入缓冲池的内容
    while True:
        epoll_list = epoll.poll(-1)  # epoll.poll会返回一个监听列表
        for fd, event in epoll_list:
            if fd == new_server.fileno():
                message = new_server.recv(100)  # recv返回字节流信息
                if message:
                    print(message.decode("utf8"))
                else:
                    return

            elif fd == sys.stdin.fileno():
                try:
                    stance = input()
                except EOFError:    # 当对方用户执行ctrl+d时退出，会返回空内容，这时断开本地
                    print("已退出")
                    return
                new_server.send(stance.encode("utf8"))  # send()内容之需要填入字节流
    new_server.close()
    sever.close()


if __name__ == '__main__':
    TCP_server()
