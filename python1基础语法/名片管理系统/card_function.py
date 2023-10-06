list_user = []


def menu():
    """显示菜单"""
    print('*' * 50)
    print("欢迎使用名片管理系统！\n您可以输入数字执行以下操作：\n1.新建名片\n2.显示全部\n3.查询名片\n0.退出系统")
    print('*' * 50)


def add_user():
    """新建用户"""
    print('-' * 50)
    print("请填写新键用户的相关信息：")
    name = input("用户姓名：")
    phone = input("用户电话：")
    QQ = input("用户QQ：")
    post = input("用户邮箱：")
    user_message = {"姓名": name, "电话": phone, "QQ": QQ, "邮箱": post}
    list_user.append(user_message)
    print("用户已添加！")
    print('-' * 50)


def showal_user():
    print('-' * 50)
    print("所有用户信息如下：")
    print("姓名".ljust(12), end="")
    print("电话".ljust(12), end="")
    print("QQ".ljust(12), end="")
    print("邮箱".ljust(12))
    for i in list_user:
        for j in i.values():
            print(j.ljust(12), end="")
    print()
    print('-' * 50)


def check_user():
    name = input("请输入您要查询的姓名：")
    for i in list_user:
        if i.name == name:
            print(i)


if __name__ == '__main__':
    menu()
