import os


def use_file():
    # 以下形式打开文件，默认是打开文本文件
    file = open('file.txt', mode='w+', encoding='utf8')
    file.write("人生苦短，我用Python！\n你呢？")
    file.seek(0)  # 不能没有参数，默认的后面一个参数是0
    stance = file.read()  # read()内部不加参数，默认是光标处读取到全部内容
    print(stance)
    file.close()


def re_file():
    os.rename('file.txt', 'file1.txt')


if __name__ == '__main__':
    use_file()
    re_file()
