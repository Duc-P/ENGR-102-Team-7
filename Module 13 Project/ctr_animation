import pygame
# NEEDED FOR EVERY FILE
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

cup = pygame.image.load('cup.png')
cup_small = pygame.transform.scale(cup, (50, 50))
#Left Cup
class ctr_left_cup:
    def __init__(self, x, y, a, x_i, y_i, image):
        self.x = x
        self.y = y
        self.velo = a
        self.x_i = x_i
        self.y_i = y_i
        self.image = image
        self.ctr_left_move1 = True
        self.ctr_left_move2 = False
        self.ctr_left_move3 = False
    def draw(self):
        SCREEN.blit(self.image,(self.x, self.y))
    def update(self):'''
        if self.ctr_left_move1:
            self.y -= self.velo
            if self.y <= SCREEN.get_height()/4:
                self.ctr_left_move1 = False
                self.ctr_left_move2 = True
        if self.ctr_left_move2:
            self.x += self.velo
            if self.x >= SCREEN.get_width()/2:
                self.ctr_left_move2 = False
                self.ctr_left_move3 = True
        if self.ctr_left_move3:
            self.y += self.velo
            if self.y >= SCREEN.get_height()/2:
                self.ctr_left_move3 = False
        if (not self.ctr_left_move3) and (not self.ctr_left_move2) and (not self.ctr_left_move1):
            self.y = self.y_i
            self.x = self.x_i'''

#MIDDLE CUP

class ctr_mid_cup:
    def __init__(self, x, y, a, x_i, y_i, image):
        self.x = x
        self.y = y
        self.velo = a
        self.x_i = x_i
        self.y_i = y_i
        self.image = image
        self.ctr_mid_move1 = True
        self.ctr_mid_move2 = False
        self.ctr_mid_move3 = False
    def draw(self):
        SCREEN.blit(self.image,(self.x, self.y))
    def update(self):
        if self.ctr_mid_move1:
            self.y += self.velo
            if self.y >= (SCREEN.get_height()/4)*3:
                self.ctr_mid_move1 = False
                self.ctr_mid_move2 = True
        if self.ctr_mid_move2:
            self.x += self.velo
            if self.x >= (SCREEN.get_width()/3)*2:
                self.ctr_mid_move2 = False
                self.ctr_mid_move3 = True
        if self.ctr_mid_move3:
            self.y -= self.velo
            if self.y <= SCREEN.get_height()/2:
                self.ctr_mid_move3 = False
        if (not self.ctr_mid_move3) and (not self.ctr_mid_move2) and (not self.ctr_mid_move1):
            self.y = self.y_i
            self.x = self.x_i

                
#RIGHT CUP
class ctr_right_cup:
    def __init__(self, x, y, a, x_i, y_i, image):
        self.x = x
        self.y = y
        self.velo = a
        self.x_i = x_i
        self.y_i = y_i
        self.image = image
        self.ctr_right_move1 = True
        self.ctr_right_move2 = False
        self.ctr_right_move3 = False
    def draw(self):
        SCREEN.blit(self.image,(self.x, self.y))
    def update(self):
        if self.ctr_right_move1:
            self.y -= self.velo
            if self.y <= (SCREEN.get_height()/4):
                self.ctr_right_move1 = False
                self.ctr_right_move2 = True
        if self.ctr_right_move2:
            self.x -= self.velo
            if self.x <= SCREEN.get_width()/2:
                self.ctr_right_move2 = False
                self.ctr_right_move3 = True
        if self.ctr_right_move3:
            self.y += self.velo
            if self.y >= SCREEN.get_height()/2:
                self.ctr_right_move3 = False
        if (not self.ctr_right_move3) and (not self.ctr_right_move2) and (not self.ctr_right_move1):
            self.y = self.y_i
            self.x = self.x_i

the_ctr_left_cup = ctr_left_cup(SCREEN.get_width()/3, SCREEN.get_height()/2, 2, SCREEN.get_width()/3, SCREEN.get_height()/2, cup_small)
the_ctr_mid_cup = ctr_mid_cup(SCREEN.get_width()/2, SCREEN.get_height()/2, 2, SCREEN.get_width()/2, SCREEN.get_height()/2, cup_small)
the_ctr_right_cup = ctr_right_cup((SCREEN.get_width()/3)*2, SCREEN.get_height()/2, 2, (SCREEN.get_width()/3)*2, SCREEN.get_height()/2, cup_small)

def ctr_animation():
    the_ctr_left_cup.update()
    the_ctr_mid_cup.update()
    the_ctr_right_cup.update()
    the_ctr_left_cup.draw()
    the_ctr_mid_cup.draw()
    the_ctr_right_cup.draw()
