import struct
import socket


def INI_ser():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("192.168.86.20", 2000)
    server.bind(addr)
    server.listen(128)
    return server


def Run_ser():
    """以火车头+火车厢的形式发送内容"""
    server = INI_ser()
    new_client, addr_client = server.accept()
    print(f"{addr_client}已连接")
    file_name = "file1"

    new_client.send(
        struct.pack('I', len(file_name.encode("utf8"))))  # 此处pack将整型转为字节流的形式
    new_client.send(file_name.encode("utf8"))

    file = open("file1", 'rb')
    file_content = file.read()
    new_client.send(struct.pack('I', len(file_content))) # 获得内容的字节数，并将其转为字节形式发送
    new_client.send(file_content)
    file.close()
    new_client.close()
    server.close()


if __name__ == '__main__':
    Run_ser()
