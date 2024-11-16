import pygame
# NEEDED FOR EVERY FILE
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

cup = pygame.image.load('cup.png')
cup_small = pygame.transform.scale(cup, (50, 50))
#Left Cup
class rtl_left_cup:
    def __init__(self, x, y, a, x_i, y_i, image):
        self.x = x
        self.y = y
        self.velo = a
        self.x_i = x_i
        self.y_i = y_i
        self.image = image
        self.rtl_left_move1 = True
        self.rtl_left_move2 = False
        self.rtl_left_move3 = False
    def draw(self):
        SCREEN.blit(self.image,(self.x, self.y))
    def update(self):
        if self.rtl_left_move1:
            self.y -= self.velo
            if self.y <= SCREEN.get_height()/4:
                self.rtl_left_move1 = False
                self.rtl_left_move2 = True
        if self.rtl_left_move2:
            self.x += self.velo
            if self.x >= (SCREEN.get_width()/3)*2:
                self.rtl_left_move2 = False
                self.rtl_left_move3 = True
        if self.rtl_left_move3:
            self.y += self.velo
            if self.y >= SCREEN.get_height()/2:
                self.rtl_left_move3 = False
        if (not self.rtl_left_move3) and (not self.rtl_left_move2) and (not self.rtl_left_move1):
            self.y = self.y_i
            self.x = self.x_i

#MIDDLE CUP

class rtl_mid_cup:
    def __init__(self, x, y, a, x_i, y_i, image):
        self.x = x
        self.y = y
        self.velo = a
        self.x_i = x_i
        self.y_i = y_i
        self.image = image
        self.rtl_mid_move1 = True
        self.rtl_mid_move2 = False
        self.rtl_mid_move3 = False
    def draw(self):
        SCREEN.blit(self.image,(self.x, self.y))
    def update(self):
        '''if self.rtl_mid_move1:
            self.y += self.velo
            if self.y >= (SCREEN.get_height()/4)*3:
                self.rtl_mid_move1 = False
                self.rtl_mid_move2 = True
        if self.rtl_mid_move2:
            self.x += self.velo
            if self.x >= (SCREEN.get_width()/3)*2:
                self.rtl_mid_move2 = False
                self.rtl_mid_move3 = True
        if self.rtl_mid_move3:
            self.y -= self.velo
            if self.y <= SCREEN.get_height()/2:
                self.rtl_mid_move3 = False
        if (not self.rtl_mid_move3) and (not self.rtl_mid_move2) and (not self.rtl_mid_move1):
            self.y = self.y_i
            self.x = self.x_i'''

                
#RIGHT CUP
class rtl_right_cup:
    def __init__(self, x, y, a, x_i, y_i, image):
        self.x = x
        self.y = y
        self.velo = a
        self.x_i = x_i
        self.y_i = y_i
        self.image = image
        self.rtl_right_move1 = True
        self.rtl_right_move2 = False
        self.rtl_right_move3 = False
    def draw(self):
        SCREEN.blit(self.image,(self.x, self.y))
    def update(self):
        if self.rtl_right_move1:
            self.y += self.velo
            if self.y >= (SCREEN.get_height()/4)*3:
                self.rtl_right_move1 = False
                self.rtl_right_move2 = True
        if self.rtl_right_move2:
            self.x -= self.velo
            if self.x <= SCREEN.get_width()/3:
                self.rtl_right_move2 = False
                self.rtl_right_move3 = True
        if self.rtl_right_move3:
            self.y -= self.velo
            if self.y <= SCREEN.get_height()/2:
                self.rtl_right_move3 = False
        if (not self.rtl_right_move3) and (not self.rtl_right_move2) and (not self.rtl_right_move1):
            self.y = self.y_i
            self.x = self.x_i

the_rtl_left_cup = rtl_left_cup(SCREEN.get_width()/3, SCREEN.get_height()/2, 12, SCREEN.get_width()/3, SCREEN.get_height()/2, cup_small)
the_rtl_mid_cup = rtl_mid_cup(SCREEN.get_width()/2, SCREEN.get_height()/2, 12, SCREEN.get_width()/2, SCREEN.get_height()/2, cup_small)
the_rtl_right_cup = rtl_right_cup((SCREEN.get_width()/3)*2, SCREEN.get_height()/2, 12, (SCREEN.get_width()/3)*2, SCREEN.get_height()/2, cup_small)

def rtl_animation():
    the_rtl_left_cup.update()
    the_rtl_mid_cup.update()
    the_rtl_right_cup.update()
    the_rtl_left_cup.draw()
    the_rtl_mid_cup.draw()
    the_rtl_right_cup.draw()
