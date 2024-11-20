import pygame
from pygame import mixer
pygame.init()
mixer.init()
'''
vine = pygame.mixer.Sound("vine.wav")
ack = pygame.mixer.Sound("ack.wav")
button = pygame.mixer.Sound("menu-button.wav")
whoosh = pygame.mixer.Sound("whoosh.wav")
laugh = pygame.mixer.Sound("cat-laugh.wav")
pluh = pygame.mixer.Sound("pluh.wav")
getout = pygame.mixer.Sound("get-out.wav")
'''
screen_width = 900
screen_height = 700
pygame.mixer.music.load('ack.wav')
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.mixer.Channel(0).play(pygame.mixer.Sound('ack.wav'))
run = True