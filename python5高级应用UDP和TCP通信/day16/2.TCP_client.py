import socket


def TCP_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("192.168.0.103", 2000)
    client.connect(addr)
    client.send("hello!".encode('utf8'))
    message = client.recv(6)
    print(message.decode("utf8"))
    message = client.recv(100)
    print(message.decode("utf8"))
    client.close()


if __name__ == '__main__':
    TCP_client()
