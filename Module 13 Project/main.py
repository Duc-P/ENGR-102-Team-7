import pygame, sys
from button import Button

pygame.init()

user_screen = pygame.display.Info()
SCREEN = pygame.display.set_mode((user_screen.current_w, user_screen.current_h))

#SCREEN = pygame.display.set_mode((1280, 720)) #This is the screen size! 1280 by 720
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.jpg")
marble = pygame.image.load("assets/marble.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        #SCREEN.fill("white")
        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(45).render("This is the GAME screen.", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50)) 
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)#Puts "This is the GAME screen." on the top and center of the screen

        """
        for i in range (255, 0, -1):
            #SCREEN.fill((0,0,0))       
            marble.set_alpha(i)    
            SCREEN.blit(marble, (600,300))    
            pygame.display.blip() 
            time.sleep(0.001)
        """
        SCREEN.blit(marble, (600,300)) #Puts marble in middle of screen

        PLAY_BACK = Button(image=None, pos=(0.9 * user_screen.current_w, 0.9 * user_screen.current_h), 
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
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TITLE", True, "#FFFFFF")
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
                    play()
                if GUIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    guide()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
