def error():
    try:  # 输入一个整型数字，否则抛出异常
        num = int(input("请输入一个数字："))
    except ValueError:  # 一些常见的错误，进行抛出异常
        print("您输入的数据类型不对")
    except Exception as result:  # 记录那些未能考虑到的错误
        print(result)
    else:  # 没有错误时才会执行的部分
        print("正常执行！")
    finally:  # 无论如何都会执行的部分
        print("本次运行结束！")


def raise_test():  # 自定义一个异常
    num = input("请输入一个整数：")
    if type(num) == int:
        print("感谢输入！", end=' ')
        return num
    # else:
    ex = Exception("输入的不是整型！！好好看看")
    raise ex


if __name__ == '__main__':
    # error()
    # print(type(123))
    try:
        num = raise_test()
        print(num)
    except Exception as result:
        print(result)
