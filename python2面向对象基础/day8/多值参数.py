# 多值函数的形参内还是要用*，和**来接收
def demo(num, *args, **kwargs):  # 在元组前加*，即为解包, 未知参数变多
    print(num)  # 在字典前加**，即为解包，字典变为：关键字=值，的形式
    print(args)
    print(*args)
    print(kwargs)
    # print(**kwargs)


demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)
