import pygame
# NEEDED FOR EVERY FILE
SCREEN = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

cup = pygame.image.load('cup.png')
cup_small = pygame.transform.scale(cup, (150, 150))
a, b, cup_x, cup_y = cup_small.get_rect()

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
        if self.x != self.x_i or self.y != self.y_i:
            SCREEN.blit(self.image,(self.x, self.y))
    def update(self):
        if self.rtl_left_move1:
            self.y += self.velo
            if self.y >= SCREEN.get_height()/4*3-(cup_y/2):
                self.rtl_left_move1 = False
                self.rtl_left_move2 = True
        elif self.rtl_left_move2:
            self.x += self.velo
            if self.x >= (SCREEN.get_width()/3)*2-(cup_x/2):
                self.rtl_left_move2 = False
                self.rtl_left_move3 = True
        elif self.rtl_left_move3:
            self.y -= self.velo
            if self.y <= SCREEN.get_height()/2-(cup_y/2):
                self.rtl_left_move3 = False
        else:
            self.y = self.y_i
            self.x = self.x_i
    def return_position(self):
        return self.y, self.x
    def return_values(self):
        return self.x, self.y, self.x_i, self.y_i
    def reset(self):
        self.x = self.x_i
        self.y = self.y_i
        self.rtl_left_move1 = True
        self.rtl_left_move2 = False
        self.rtl_left_move3 = False
the_rtl_left_cup = rtl_left_cup((SCREEN.get_width()/3)-(cup_x/2), (SCREEN.get_height()/2)-(cup_y/2), 37, SCREEN.get_width()/3 - (cup_x/2), SCREEN.get_height()/2-(cup_y/2) , cup_small)

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
          if (the_rtl_left_cup.return_values()[0] != the_rtl_left_cup.return_values()[2]) or (the_rtl_left_cup.return_values()[1] != the_rtl_left_cup.return_values()[3]):
            SCREEN.blit(self.image,(self.x, self.y))
    def update(self):
        '''if self.rtl_mid_move1:
            self.y += self.velo
            if self.y >= (SCREEN.get_height()/4)*3-(cup_y/2):
                self.rtl_mid_move1 = False
                self.rtl_mid_move2 = True
        elif self.rtl_mid_move2:
            self.x += self.velo
            if self.x >= (SCREEN.get_width()/3)*2-(cup_x/2):
                self.rtl_mid_move2 = False
                self.rtl_mid_move3 = True
        elif self.rtl_mid_move3:
            self.y -= self.velo
            if self.y <= SCREEN.get_height()/2-(cup_y/2):
                self.rtl_mid_move3 = False
        else (not self.rtl_mid_move3) and (not self.rtl_mid_move2) and (not self.rtl_mid_move1):
            self.y = self.y_i
            self.x = self.x_i'''
    def return_values(self):
        return self.x, self.y, self.x_i, self.y_i
the_rtl_mid_cup = rtl_mid_cup(SCREEN.get_width()/2-(cup_x/2), SCREEN.get_height()/2-(cup_y/2), 37, SCREEN.get_width()/2-(cup_x/2), SCREEN.get_height()/2-(cup_y/2), cup_small)

                
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
        if self.x != self.x_i or self.y != self.y_i:
            SCREEN.blit(self.image,(self.x, self.y))
    def update(self):
        if self.rtl_right_move1:
            self.y -= self.velo
            if self.y <= (SCREEN.get_height()/4)-(cup_y/2):
                self.rtl_right_move1 = False
                self.rtl_right_move2 = True
        elif self.rtl_right_move2:
            self.x -= self.velo
            if self.x <= SCREEN.get_width()/3-(cup_x/2):
                self.rtl_right_move2 = False
                self.rtl_right_move3 = True
        elif self.rtl_right_move3:
            self.y += self.velo
            if self.y >= SCREEN.get_height()/2-(cup_y/2):
                self.rtl_right_move3 = False
        else:
            self.y = self.y_i
            self.x = self.x_i
    def return_position(self):
        return self.y, self.x
    def return_values(self):
        return self.x, self.y, self.x_i, self.y_i
    def reset(self):
        self.x = self.x_i
        self.y = self.y_i
        self.rtl_right_move1 = True
        self.rtl_right_move2 = False
        self.rtl_right_move3 = False

the_rtl_right_cup = rtl_right_cup((SCREEN.get_width()/3)*2-(cup_x/2), SCREEN.get_height()/2-(cup_y/2), 37, (SCREEN.get_width()/3)*2-(cup_x/2), SCREEN.get_height()/2-(cup_y/2), cup_small)
def rtl_animation_ccw_reset():
    the_rtl_left_cup.reset()
    the_rtl_right_cup.reset()
def rtl_animation_ccw():
    '''Takes in no input as a parameter. Updates PNGs during animation, and then subsequently prints them. Oncee the animation is done, it will stop printing the PNGs.
    This animation switches the right and the left cup in a counterclockwise motion.'''
    the_rtl_left_cup.update()
    the_rtl_mid_cup.update()
    the_rtl_right_cup.update()
    the_rtl_left_cup.draw()
    the_rtl_mid_cup.draw()
    the_rtl_right_cup.draw()