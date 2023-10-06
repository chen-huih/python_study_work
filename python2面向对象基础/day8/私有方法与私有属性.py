class A():
    def __init__(self, name, height=34):
        self.name = name
        self.__height = height

    def __set(self):
        return self.__height

    def get(self):
        return self.__height

    def ret(self):
        return self.__set()


a = A('小红', 45)
print(a.name)
print(a._A__height)  # 这种方法可以访问私有属性和方法
print('*' * 50)
print(a.get())
b = a.get()
c = a.ret()
print(b)
print(c)
