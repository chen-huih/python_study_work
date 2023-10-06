import re


def fun1():
    list1 = ['bat', 'bit', 'but', 'hat', 'hit', 'hut']
    for i in list1:
        result = re.match("[bh].t$", i)
        print(result.group())


def fun2():
    list1 = ['131231@163.com', "hfhief@1633..com", "hfae@163.com11",
             "[12@163.com", "@163.com"]
    for i in list1:
        result = re.match("[\w]+@163\.com$", i)
        if result:
            print(result.group())


def fun3():
    list1 = ['12', '34', '2341', '1', '00', '02']
    for i in list1:
        result = re.match("[1-9]?\d$", i)
        if result:
            print(result.group())


if __name__ == '__main__':
    # fun1()
    # fun2()
    # fun3()
    print(int('00'))
    print(int('02'))