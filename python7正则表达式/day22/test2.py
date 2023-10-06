import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = ("192.168.23.20", 2000)
c.connect(ip)
c.send(b"hello")
c.send(b" world")
c.close()