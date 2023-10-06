def fun1():
    num = input("请输入")
    print(num)  # ctrl+d，会退出input，即抛出异常


def fun2():
    list1 = [1, 2, 3, 4, 5]
    for i in list1:
        if i == 3:
            list1.remove(i)
        print(i)


if __name__ == '__main__':
    # fun1()
    # fun2()
    f = "ehhe"
    print(f"hee"+f)