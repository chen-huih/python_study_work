class Dog:
    def __init__(self, name, dog_color):
        self.name = name
        self.dog_color = dog_color

    def bark(self):
        print("%s在汪汪叫" % self.name)

    def action(self):
        print("%s在摇尾巴" % self.name)

    def __str__(self):
        return "%s是一个%s的狗狗" % (self.name, self.dog_color)


yellow = Dog('大黄', '黄色')
yellow.bark()
yellow.action()
print(yellow)
print(dir(Dog))