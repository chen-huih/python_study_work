class cyc_queue():
    def __init__(self, len):
        self.len = len + 1
        self.queue = [0] * self.len
        self.first = 0
        self.last = 0
        print("初始化成功：")
        print(self.queue)

    def add_value(self, value):
        if (self.last + 1)%self.len != self.first:
            self.queue[self.last] = value
            self.last = (self.last + 1) % self.len
            print("元素添加成功：")
            self.show()
        else:
            print("列表已满")

    def pop_value(self):
        if self.first != self.last:
            num = self.queue[self.first]
            self.first = (self.first + 1) % self.len
            return num
        else:
            print("列表为空！")

    def show(self):
        if self.first <= self.last:
            for i in range(self.first, self.last):
                print(self.queue[i], end=' ')
            print()
        else:
            for i in range(self.first, self.len):
                print(self.queue[i], end='')
            for i in range(0, self.last):
                print(self.queue[i], end='')
            print()


if __name__ == '__main__':
    q1 = cyc_queue(5)
    for i in range(1,8):
        q1.add_value(i)
    for i in range(6):
        print(q1.pop_value())
        q1.show()
