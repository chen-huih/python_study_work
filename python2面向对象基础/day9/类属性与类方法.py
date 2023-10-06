class Test:
    count = 0  # 类属性

    def __init__(self):
        Test.count += 1

    @classmethod    # 类方法
    def fun1(cls):
        print(cls.count)


if __name__ == '__main__':
    print(Test.count)
    a = Test()
    b = Test()
    print(a.count)
    a.fun1()
