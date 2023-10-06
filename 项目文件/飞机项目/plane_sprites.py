import pygame
import random
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
CREAT_ENEMY = pygame.USEREVENT
FIRE_BULLET = pygame.USEREVENT + 1


class GameSprites(pygame.sprite.Sprite):
    def __init__(self, image_path, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        pass


class BackGrand_Sprites(GameSprites):
    def __init__(self, flag: bool = False):
        super().__init__('./images/background.png')
        if flag:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy_Sprites(GameSprites):
    def __init__(self, speed = 1):
        super().__init__('./images/enemy1.png', speed)
        self.rect.y = -self.rect.height
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)#SCREEN_RECT.width - self.rect.width

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_RECT.bottom:
            print('敌机飞过')
            self.kill()

    def __del__(self):
        print('消灭一个敌机')


class Ship_Sprites(GameSprites):
    def __init__(self):
        super().__init__('./images/me1.png')
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.rect.centerx = SCREEN_RECT.centerx
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        super().update()
        self.rect.x += self.speed
        if self.rect.left <= SCREEN_RECT.left:
            self.rect.left = SCREEN_RECT.left
        if self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        bullet = Bullet_Sprites()
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.y = self.rect.y - 20
        self.bullet_group.add(bullet)


class Bullet_Sprites(GameSprites):
    def __init__(self):
        super().__init__('./images/bullet2.png')

    def update(self):
        super().update()
        self.rect.y -= 2
        if self.rect.y <= 0:
            self.kill()


if __name__ == '__main__':
    for i in range(0,10):
        print(random.rand)
