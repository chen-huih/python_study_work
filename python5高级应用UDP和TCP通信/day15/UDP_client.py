import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "王总好，"
c.sendto(message.encode('utf8'), ('192.168.0.103', 2000))
back_message = c.recvfrom(100)
print(back_message[0].decode('utf8'))
c.close()
