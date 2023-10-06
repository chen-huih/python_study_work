from socket import *
from multiprocessing import Pool
import struct
import os


class server:
    def __init__(self, ip="", port=2000):
        self.s_link: socket = None
        self.addr = (ip, port)
        self.poll = Pool(5)  # 进程池与面向对象结合的并不好，进程池可以直接放到主方法中

    def tcp_init(self):
        self.s_link = socket(AF_INET, SOCK_STREAM)
        self.s_link.bind(self.addr)
        self.s_link.listen(128)

    def tack(self):
        user = User(self.s_link)
        # user.deal_act()
        self.poll.apply_async(run_pro, args=(user,))    # 该方法需要传入一个直接方法


class User:

    def __init__(self, s_link: socket):
        self.client, self.client_addr = s_link.accept()
        print(f"{self.client_addr}连接成功")
        self.path = os.getcwd()

    def deal_act(self):
        while True:
            user_act = self.recv_train().decode("utf8")
            if user_act.split()[0] == "ls":
                self.do_ls()
            elif user_act.split()[0] == "cd":
                self.do_cd(user_act.split()[1])
            elif user_act.split()[0] == "pwd":
                self.do_pwd()
            elif user_act.split()[0] == "rm":
                self.do_rm(user_act.split()[1])
            elif user_act.split()[0] == "puts":
                self.do_puts(user_act.split()[1])
            elif user_act.split()[0] == "gets":
                self.do_gets(user_act.split()[1])

    def do_ls(self):
        data = ''
        for i in os.listdir(self.path):
            data += i + " " * 5 + str(os.stat(i).st_size) + "\n"
        self.send_train(data.encode("utf8"))

    def do_cd(self, new_path):
        os.chdir(new_path)  # 真正切换路径
        self.path = os.getcwd()  # 得到当前路径
        self.send_train(f"切换目录到{self.path}".encode("utf8"))

    def do_pwd(self):
        self.send_train(self.path.encode("utf8"))

    def do_rm(self, file):
        os.remove(file)
        self.send_train(f"文件{file}已被删除！".encode("utf8"))

    def do_gets(self, file):
        f = open(file, "rb")
        file_content = f.read()
        f.close()
        self.send_train(file_content)

    def do_puts(self, file_name):
        file = open(file_name, "wb")
        file_content = self.recv_train()
        file.write(file_content)
        file.close()

    def send_train(self, message):
        """发火车"""

        head_bytes = struct.pack('I',
                                 len(message))  # 此处pack将整型转为字节流的形式
        self.client.send(head_bytes + message)

    def recv_train(self):
        """收火车"""
        lens = self.client.recv(4)
        content = self.client.recv(struct.unpack("I", lens)[0])
        return content


def run_pro(user_link):  # 直接定义方法而不是对象方法
    user_link.deal_act()


if __name__ == '__main__':
    s = server('192.168.231.20')
    s.tcp_init()
    while True:
        s.tack()
    self.poll.close()
    self.poll.join()
