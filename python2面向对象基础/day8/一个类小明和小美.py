class Person():
    def __init__(self, name: str, like_run: bool, weight, height = 67):
        self.name = name
        self.like_run = like_run
        self.height = height
        self.weight = weight

    def run(self):
        if self.like_run:
            print("%s喜欢跑步" % self.name)
        else:
            print("%s不喜欢跑步" % self.name)

    def eat(self):
        print("%s在吃东西" % self.name)

    def __str__(self):
        return "%s的身高是%.3f,体重为%.3f" % (self.name, self.height, self.weight)


xiaoming = Person('小明', True, 56.32,188)
xiaoming.run()
xiaoming.eat()
print(xiaoming)
xiaohong = Person('小红', False, 160, 56.33)
xiaohong.run()
xiaohong.eat()
print(xiaohong)
