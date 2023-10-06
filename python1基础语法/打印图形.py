def malp_1():
    """打印菱形"""
    for i in range(1, 10):
        num = abs(i - 5)
        for j in range(num):
            print(" ", end="")
        if i <= 5:
            for j in range(i):
                print("* ", end="")
        else:
            for j in range(10 - i):
                print("* ", end="")
        print("")


def malp_2():
    """
    打印空心菱形
    """
    for i in range(1, 10):
        num = abs(i - 5)
        for j in range(num):
            print(" ", end="")
        if i <= 5:
            for j in range(i):
                if  i>=3 and 0<j<i-1:
                    print("  ", end="")
                else:
                    print("* ", end="")
        else:
            for j in range(10 - i):
                if 0 < j < 10 - i - 1:
                    print("  ", end="")
                else:
                    print("* ", end="")
        print("")


if __name__ == '__main__':
    malp_1()
    print('*'*50)
    malp_2()
