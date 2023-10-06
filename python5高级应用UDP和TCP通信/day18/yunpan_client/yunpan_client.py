from socket import *
import struct
import os


class User:
    def __init__(self, ip="", port=2000):
        self.c_link: socket = None
        self.addr = (ip, port)

    def tcp_init(self):
        self.c_link = socket(AF_INET, SOCK_STREAM)
        self.c_link.connect(self.addr)

    def deal_act(self):
        while True:
            user_act = input()
            self.send_train(user_act.encode("utf8"))
            if user_act.split()[0] == "ls":
                self.do_ls()
            elif user_act.split()[0] == "cd":
                self.do_cd()
            elif user_act.split()[0] == "pwd":
                self.do_pwd()
            elif user_act.split()[0] == "rm":
                self.do_rm()
            elif user_act.split()[0] == "puts":
                self.do_puts(user_act.split()[1])
            elif user_act.split()[0] == "gets":
                self.do_gets(user_act.split()[1])

    def do_ls(self):
        message = self.recv_train().decode("utf8")
        print(message)

    def do_cd(self):
        message = self.recv_train().decode("utf8")
        print(message)

    def do_pwd(self):
        message = self.recv_train().decode("utf8")
        print(message)

    def do_rm(self):
        message = self.recv_train().decode("utf8")
        print(message)

    def do_gets(self, file):
        file_content = self.recv_train()
        f = open(file, "wb")
        f.write(file_content)
        f.close()

    def do_puts(self, file):
        file1 = open(file, "rb")
        file_content = file1.read()
        self.send_train(file_content)
        file1.close()

    def send_train(self, message):
        """发火车"""

        head_bytes = struct.pack('I',
                                 len(message))  # 此处pack将整型转为字节流的形式
        self.c_link.send(head_bytes + message)

    def recv_train(self):
        """收火车"""
        lens = self.c_link.recv(4)
        content = self.c_link.recv(struct.unpack("I", lens)[0])
        return content


if __name__ == '__main__':
    c = User('192.168.231.20')
    c.tcp_init()
    c.deal_act()


