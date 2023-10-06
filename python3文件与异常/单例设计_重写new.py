# 单例模式是为了让一个类创建的对象都指向同一个空间
class PlayMusic:
    stance = None

    def __new__(cls, *args, **kwargs):
        if cls.stance is None:
            cls.stance = super().__new__(cls)  # 这一句记住，调用父类的方法
        return cls.stance

    def __init__(self, music):
        self.music = music


if __name__ == '__main__':  # 如果以下代码没有缩进的话，那么在import该模块后，执行时以下代码都执行
    play1 = PlayMusic("张国荣")
    print(play1.music)
    play2 = PlayMusic("你欸笑傲前")
    print(play1)
    print(play2)
    print(play2.music)
