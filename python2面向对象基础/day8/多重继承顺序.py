class A():
    def __init__(self):
        self.num = 10
        self.__num1 = 4

    def run(self):
        print("A在跑")

    def eat(self):
        print("A在吃")


class B():
    def __init__(self):
        self.num = 20
        self.num2 = 13

    def run(self):
        print("B在跑")

    def eat(self):
        print("B在吃")
    def harf(self):
        print("B在笑")


class C(A, B):
    def bark(self):
        print("C在叫")


if __name__ == '__main__':
    c = C()
    c.eat()
    c.run()
    c.bark()
    c.harf()
    print(c.num)
    #print(c.num2)  # 执行A的__init__的，而不是B的init
