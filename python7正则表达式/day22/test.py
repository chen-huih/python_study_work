import socket
def fun():
    try:
        num = input("输入")
        num += 1
        print(num)
    except Exception as e:
        print(e)
    print("hhhhhh")
def server():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip = ("192.168.23.20", 2000)
    s.bind(ip)
    s.listen(128)
    new_client,addr = s.accept()
    content = new_client.recv(20)
    print(content)
    s.close()
if __name__ == '__main__':
    server()