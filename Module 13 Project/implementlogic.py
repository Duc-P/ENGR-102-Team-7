import pygame, sys
import time
from button import Button
from animation_ctl import ctl_animation
from animation_ctr import ctr_animation
from animation_rtl import rtl_animation
from shuffle_logic import place_marble


pygame.init()

user_screen = pygame.display.Info()
SCREEN = pygame.display.set_mode((user_screen.current_w, user_screen.current_h))

#SCREEN = pygame.display.set_mode((1280, 720)) #This is the screen size! 1280 by 720
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.jpg")
marble = pygame.image.load("assets/marble.png")
marble_small_l = pygame.transform.scale(marble, (50,50))
marble_small_m = pygame.transform.scale(marble, (50,50))
marble_small_r = pygame.transform.scale(marble, (50,50))
a,b,marble_x,marble_y=marble_small_l.get_rect()
cup_transparent = pygame.image.load('assets/cup.png')
cup_transparent.set_alpha(0)
cup_small_transparent = pygame.transform.scale(cup_transparent, (150, 150))
a,b,cup_x,cup_y=cup_small_transparent.get_rect()
vine = pygame.mixer.Sound("assets/vine.wav")
ack = pygame.mixer.Sound("assets/ack.wav")
button_sound = pygame.mixer.Sound("assets/menu-button.wav")
clock = pygame.time.Clock()


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        clock.tick(60)
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("white")
        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(45).render("This is the GAME screen.", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50)) 
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)#Puts "This is the GAME screen." on the top and center of the screen

        
        button_l = Button(image=cup_small_transparent, pos=[(SCREEN.get_width()/3) + (cup_x)/2, (SCREEN.get_height()/2) + (cup_y/2)], text_input="", font=get_font(0), base_color="Black", hovering_color="Black")
        button_m = Button(image=cup_small_transparent, pos=[(SCREEN.get_width()/2) + (cup_x)/2, (SCREEN.get_height()/2) + (cup_y/2)], text_input="", font=get_font(0), base_color="Black", hovering_color="Black")
        button_r = Button(image=cup_small_transparent, pos=[((SCREEN.get_width()/3) * 2) + (cup_x)/2, (SCREEN.get_height()/2) + (cup_y/2)], text_input="", font=get_font(0), base_color="Black", hovering_color="Black")

        ctl_animation()
        marble_small_l.set_alpha(0)
        marble_small_m.set_alpha(0)
        marble_small_r.set_alpha(0)
        SCREEN.blit(marble_small_l, ((SCREEN.get_width()/3) + (marble_x)/2, (SCREEN.get_height()/2) + (marble_y/2)))
        SCREEN.blit(marble_small_m, ((SCREEN.get_width()/2) + (marble_x)/2, (SCREEN.get_height()/2) + (marble_y/2)))
        SCREEN.blit(marble_small_r, (((SCREEN.get_width()/3) * 2) + (marble_x)/2, (SCREEN.get_height()/2) + (marble_y/2)))

        #SCREEN.blit(marble, (600,300)) #Puts marble in middle of screen
        """[(SCREEN.get_width()/3) + (cup_x)/2, (SCREEN.get_height()/2) + (cup_y/2)]
        [(SCREEN.get_width()/2) + (cup_x)/2, (SCREEN.get_height()/2) + (cup_y/2)]
        [((SCREEN.get_width()/3) * 2) + (cup_x)/2, (SCREEN.get_height()/2) + (cup_y/2)]
        
        if summonme == True:
            SCREEN.blit(marble, (100, 300))
            for i in range (255, 0, -1):
                marble.set_alpha(i)
                PLAY_BACK.update(SCREEN)
                PLAY_Test.update(SCREEN)
                pygame.display.update()
                pygame.time.delay(1)
        """
        

        """
        time.sleep(0.001)
        for i in range (255, 0, -1):
            marble.set_alpha(i)
            time.sleep(0.001)
        
        for i in range (255, 0, -1):
            SCREEN.blit(PLAY_TEXT, PLAY_RECT)       
            marble.set_alpha(i)    
            #SCREEN.blit(marble, (600,300))    
            #pygame.display.blip() 
            time.sleep(0.001)
        """
        

        PLAY_BACK = Button(image=None, pos=(0.9 * user_screen.current_w, 0.9 * user_screen.current_h), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        PLAY_TEST = Button(image=None, pos=(0.9 * user_screen.current_w, 0.8 * user_screen.current_h), 
                            text_input="TEST", font=get_font(75), base_color="Black", hovering_color="Green")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        #PLAY_TEST.changeColor(PLAY_MOUSE_POS)
        #PLAY_TEST.update(SCREEN)
        button_l.update(SCREEN)
        button_m.update(SCREEN)
        button_r.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
               # if PLAY_TEST.checkForInput(PLAY_MOUSE_POS):
                    #summonme = True
                    #SCREEN.blit(marble, (100, 300))
                    for i in range (255, 0, -1):
                        marble.set_alpha(i)
                        PLAY_BACK.update(SCREEN)
                        PLAY_TEST.update(SCREEN)
                        pygame.display.update()
                        pygame.time.delay(1)
                if button_l.checkForInput(PLAY_MOUSE_POS):
                    #place_marble(0, 2)
                    abc = place_marble(0, 2)
                    print(0)
                    print(abc)
                    if abc.index(True) == 0:
                        marble_small_l.set_alpha(255)
                        print("A")
                        SCREEN.blit(marble_small_l, ((SCREEN.get_width()/3) + (marble_x)/2, (SCREEN.get_height()/2) + (marble_y/2)))
                        pygame.display.update()
                    elif abc.index(True) == 1:
                        marble_small_m.set_alpha(255)
                        print("B")
                        SCREEN.blit(marble_small_m, ((SCREEN.get_width()/2) + (marble_x)/2, (SCREEN.get_height()/2) + (marble_y/2)))
                        pygame.display.update()
                    else:
                        marble_small_r.set_alpha(255)
                        print("C")
                        SCREEN.blit(marble_small_r, (((SCREEN.get_width()/3) * 2) + (marble_x)/2, (SCREEN.get_height()/2) + (marble_y/2)))
                        pygame.display.update()
                if button_m.checkForInput(PLAY_MOUSE_POS):
                    #place_marble(1, 2)
                    abc = place_marble(1, 2)
                    print(1)
                    print(abc)
                if button_r.checkForInput(PLAY_MOUSE_POS):
                    #place_marble(2, 2)
                    place_marble(2, 2)
                    print(2)
                    print(abc)


        
        pygame.display.update()
    
def guide():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        GUIDE_TEXT = get_font(45).render("This is the USER GUIDE.", True, "Black")
        GUIDE_RECT = GUIDE_TEXT.get_rect(center=(0.5 * user_screen.current_w, 0.1 * user_screen.current_h))
        SCREEN.blit(GUIDE_TEXT, GUIDE_RECT)
        
        GUIDE_TEXT2 = get_font(45).render("1) Put a marble in any of the three boxes.", True, "Black")
        GUIDE_RECT2 = GUIDE_TEXT.get_rect(center=(0.25 * user_screen.current_w, 0.2 * user_screen.current_h))
        SCREEN.blit(GUIDE_TEXT2, GUIDE_RECT2)
        
        GUIDE_TEXT3 = get_font(45).render("2) The boxes will shuffle randomly.", True, "Black")
        GUIDE_RECT3 = GUIDE_TEXT.get_rect(center=(0.25 * user_screen.current_w, 0.3 * user_screen.current_h))
        SCREEN.blit(GUIDE_TEXT3, GUIDE_RECT3)
        
        GUIDE_TEXT4 = get_font(45).render("3) You will guess the box the marble is in.", True, "Black")
        GUIDE_RECT4 = GUIDE_TEXT.get_rect(center=(0.25 * user_screen.current_w, 0.4 * user_screen.current_h))
        SCREEN.blit(GUIDE_TEXT4, GUIDE_RECT4)
        
        GUIDE_TEXT4 = get_font(45).render("    Correct answers increase your score.", True, "Black")
        GUIDE_RECT4 = GUIDE_TEXT.get_rect(center=(0.25 * user_screen.current_w, 0.45 * user_screen.current_h))
        SCREEN.blit(GUIDE_TEXT4, GUIDE_RECT4)
        
        GUIDE_TEXT5 = get_font(45).render("4) Once finished, press BACK to return to ", True, "Black")
        GUIDE_RECT5 = GUIDE_TEXT.get_rect(center=(0.25 * user_screen.current_w, 0.55 * user_screen.current_h))
        SCREEN.blit(GUIDE_TEXT5, GUIDE_RECT5)
        
        GUIDE_TEXT6 = get_font(45).render("    the main screen and press QUIT to exit.", True, "Black")
        GUIDE_RECT6 = GUIDE_TEXT.get_rect(center=(0.25 * user_screen.current_w, 0.6 * user_screen.current_h))
        SCREEN.blit(GUIDE_TEXT6, GUIDE_RECT6)

        GUIDE_BACK = Button(image=None, pos=(0.9 * user_screen.current_w, 0.9 * user_screen.current_h), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        GUIDE_BACK.changeColor(OPTIONS_MOUSE_POS)
        GUIDE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GUIDE_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    button_sound.play()
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("SHELLSHOCK", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(0.5 * user_screen.current_w, 0.15 * user_screen.current_h))

        PLAY_BUTTON = Button(image=None, pos=(0.5 * user_screen.current_w, 0.4 * user_screen.current_h), 
                            text_input="PLAY!", font=get_font(75), base_color="#FFFFFF", hovering_color="Green")
        GUIDE_BUTTON = Button(image=None, pos=(0.5 * user_screen.current_w, 0.6 * user_screen.current_h), 
                            text_input="USER GUIDE", font=get_font(75), base_color="#FFFFFF", hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(0.5 * user_screen.current_w, 0.8 * user_screen.current_h), 
                            text_input="QUIT", font=get_font(75), base_color="#FFFFFF", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, GUIDE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    button_sound.play()
                    marble.set_alpha(255)
                    play()
                elif GUIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    button_sound.play()
                    guide()
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    button_sound.play()
                    pygame.quit()
                    sys.exit()
                else:
                    vine.play()

        pygame.display.update()

main_menu()

"""
#import time

self.image = self.original_image.copy()
# this works on images with per pixel alpha too
alpha = 128
self.image.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)

for i in range (255, 0, -1):
    screen.fill((0,0,0))       
    image.set_alpha(i)    
    screen.blit(image, centered_image)    
    pygame.display.update()    
    time.sleep(0.001)
"""