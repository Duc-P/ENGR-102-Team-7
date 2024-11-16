import pygame
from pygame import mixer
pygame.init()
mixer.init
vine = pygame.mixer.Sound("vine.wav")
ack = pygame.mixer.Sound("ack.wav")
button = pygame.mixer.Sound("menu-button.wav")
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
run = True
while run:
    vine.play()
    ack.play()
    button.play()
    