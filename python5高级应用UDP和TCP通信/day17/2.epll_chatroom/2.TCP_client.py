import socket
import select
import sys


def TCP_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if len(sys.argv) == 1:
        addr = ('', 2000)
    else:
        addr = (sys.argv[1], 2000)
    client.connect(addr)
    epoll = select.epoll()  # 一个epoll可以并发的监听多个
    epoll.register(client.fileno(), select.EPOLLIN)  # 监听该连接的缓冲池收到的内容
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)  # 监听输入缓冲池的内容
    while True:
        epoll_list = epoll.poll(-1)  # epoll.poll会返回一个监听列表
        for fd, event in epoll_list:
            if fd == client.fileno():
                message = client.recv(100)  # recv返回字节流信息
                if message:
                    print(message.decode("utf8"))
                else:
                    print("服务器断开")
                    return
            elif fd == sys.stdin.fileno():
                try:
                    stance = input()
                except EOFError:
                    print("断开")
                    return
                client.send(stance.encode("utf8"))  # send()内容之需要填入字节流
    client.close()


if __name__ == '__main__':
    TCP_client()
