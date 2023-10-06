import struct
import socket


def INI_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("192.168.86.20", 2000)
    client.connect(addr)
    file_name_head = client.recv(4)
    file_name = client.recv(struct.unpack("I", file_name_head)[0])
    print(file_name)
    file1 = open(file_name, "wb")
    file_head = client.recv(4)
    file = client.recv(struct.unpack("I", file_head)[0])
    file1.write(file)
    file1.close()
    client.close()


if __name__ == '__main__':
    INI_client()
