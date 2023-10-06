# 作者: 王道 龙哥
# 2022年03月04日16时50分54秒

from socket import *
import struct

def tcp_init():
    s = socket(AF_INET, SOCK_STREAM)
    addr = ('', 2000)
    s.bind(addr)
    s.listen(128)
    return s

def send_file():
    file_name='file.mp4'
    s=tcp_init()
    new_client,client_addr=s.accept()
    # 先发文件名
    file_name_bytes=file_name.encode('utf8')
    train_head_bytes=struct.pack('I',len(file_name_bytes))
    new_client.send(train_head_bytes+file_name_bytes)
    # 再发文件内容，用rb方式打开，不可以用readline
    f=open(file_name,'rb')
    while True:
        file_content=f.read(1000)
        if file_content:
            train_head_bytes = struct.pack('I', len(file_content))
            new_client.send(train_head_bytes+file_content)
        else:
            train_head_bytes = struct.pack('I', 0)
            new_client.send(train_head_bytes)
            break
    f.close()
    new_client.close()
    s.close()



if __name__ == '__main__':
    send_file()