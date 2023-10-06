import 单例设计_重写new as test
from page_test import page_moudle1, page_moudle2


def main():
    print("这里是主流程代码")


# 所有没有缩进的代码都会被执行，所以规范的代码要有main函数
if __name__ == '__main__':  # 在这之下的代码不会被导入
    main()
    page_moudle1.m1()
    page_moudle2.m2()
    print(test.__name__)
