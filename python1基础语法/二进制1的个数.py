# 二进制bin(),八进制oct(),十六进制hex()
def sum_1():
    """
    这个函数求二进制中1的个数
    :return:
    """
    sum = 0
    num = input("请输入一个整数，将返回它的二进制中1的个数:")
    num = int(num)
    print(bin(num))
    for i in range(65):
        if (num&1)==1:
            sum = sum + 1
        num = num >> 1
    print("该数二进制中1的个数为%d" % sum)


if __name__ == '__main__':
    sum_1()
