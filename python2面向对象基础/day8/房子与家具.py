class furniture():
    def __init__(self, fur_name, fur_area):
        self.fur_name = fur_name
        self.fur_area = fur_area


class room():
    def __init__(self, type, area):
        self.type = type
        self.area = area
        self.free_area = area
        self.furniture = []

    def add_fur(self, furniture: furniture):
        if self.free_area >= furniture.fur_area:
            self.furniture.append(furniture.fur_name)
            self.free_area -= furniture.fur_area
        else:
            pass

    def get_freearea(self):
        print(self.free_area)

    def __str__(self):
        print("%s" % self.furniture)
        return "这是一套%s,面积是%.2f,还剩%.2f" % (
        self.type, self.area, self.free_area)


sofa = furniture('沙发', 10)
table = furniture('桌子', 5)
beijing = room('四合院', 100)
chongqing = room('公寓', 95)
print(beijing)
beijing.add_fur(sofa)
print(beijing)
beijing.add_fur(table)
print(beijing)
