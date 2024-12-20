import pygame, sys
from button import Button

from animation_rtl import animation_rtl
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720)) #This is the screen size! 1280 by 720
pygame.display.set_caption("Menu")

BG = pygame.image.load("Background.jpg")
marble = pygame.image.load("marble.png")

clock = pygame.time.Clock()

def get_font(size):
    return pygame.font.Font("font.ttf", size)

def play():
    while True:
        clock.tick(60)
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        PLAY_TEXT = get_font(45).render("This is the GAME screen.", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50)) 
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)#Puts "This is the GAME screen." on the top and center of the screen

        SCREEN.blit(marble, (600,300)) #Puts marble in middle of screen
        ## ADDING THE ANIMATION

        rtl_animation()

        ##
        PLAY_BACK = Button(image=None, pos=(1125, 670), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def guide():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        GUIDE_TEXT = get_font(45).render("This is the USER GUIDE.", True, "Black")
        GUIDE_RECT = GUIDE_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(GUIDE_TEXT, GUIDE_RECT)

        GUIDE_BACK = Button(image=None, pos=(1125, 670), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        GUIDE_BACK.changeColor(OPTIONS_MOUSE_POS)
        GUIDE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GUIDE_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TITLE", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=None, pos=(640, 250), 
                            text_input="PLAY!", font=get_font(75), base_color="#FFFFFF", hovering_color="Green")
        GUIDE_BUTTON = Button(image=None, pos=(640, 400), 
                            text_input="USER GUIDE", font=get_font(75), base_color="#FFFFFF", hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(640, 550), 
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
                    play()
                if GUIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    guide()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
