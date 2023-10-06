import pygame
from plane_sprites import *
import time


class PlaneGame():
    """游戏大战主游戏类"""

    def __init__(self):
        print('游戏初始化')
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)     # 创建屏幕，所有对象通过矩形控制，在屏幕上显示
        self.clock = pygame.time.Clock()
        self.__creat_sprites()

        pygame.time.set_timer(CREAT_ENEMY, 1000)  # 每1000毫秒，发生该事件
        pygame.time.set_timer(FIRE_BULLET, 500)  # 每500毫秒，发射子弹

    def __creat_sprites(self):
        bg1 = BackGrand_Sprites()
        bg2 = BackGrand_Sprites(True)
        self.hero = Ship_Sprites()
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.emeny_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print('开始游戏。。')
        while True: # 游戏的运行就是不断循环执行
            self.clock.tick(60)             # 刷新率，每秒执行的次数
            self.__event_check()            # 监听动作
            self.__crack_check()            # 监听碰撞
            self.__update_sprites()         # 刷新精灵
            pygame.display.update()         # 绘制屏幕

    def __event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over(self)
            elif event.type == FIRE_BULLET:
                self.hero.fire()
            elif event.type == CREAT_ENEMY:
                print("出现敌机")
                emeny = Enemy_Sprites(2)
                self.emeny_group.add(emeny)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __crack_check(self):
        # 精灵组与精灵组发生碰撞
        pygame.sprite.groupcollide(self.hero.bullet_group, self.emeny_group, True,True)
        # 精灵与精灵组发生碰撞，这个True会移除精灵组中发生碰撞的精灵。
        enemies = pygame.sprite.spritecollide(self.hero, self.emeny_group, True)
        # 因为不会移除发生碰撞的精灵，所以需要特意处理一下
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 加入声音
            m = "./sound/use_bomb.wav"
            pygame.mixer.music.load(m)
            pygame.mixer.music.play()
            time.sleep(2)
            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        for group in [self.back_group, self.emeny_group, self.hero_group]:
            group.update()
            group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    def __update_screen(self):
        pass

    def __game_over(self):
        print('游戏结束')
        pygame.quit()
        exit()


if __name__ == '__main__':
    pygame.init()
    game = PlaneGame()
    game.start_game()
