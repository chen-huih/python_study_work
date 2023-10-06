import pygame
import time
pygame.init()
m = "./sound/use_bomb.wav"
pygame.mixer.music.load(m)
n = "./sound/bullet.wav"
pygame.mixer.music.load(n)
m = "./sound/button.wav"
pygame.mixer.music.load(m)
m = "./sound/game_music.ogg"
pygame.mixer.music.load(m)
pygame.mixer.music.play()
time.sleep(5)