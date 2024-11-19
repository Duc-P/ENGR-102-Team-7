# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names:
# Townsend Wheeler
# Duc Pham
# Julian Curry
# Archelaus Paxon
# Section: 518
# Assignment: Lab Topic 13
# Date: 17-11-2024

###############
### IMPORTS ###
###############
import pygame
import sys
from button import Button

# import animations
from animation_rtl import rtl_animation
from animation_ctl import ctl_animation
from animation_ctr import ctr_animation


########################
### HELPER FUNCTIONS ###
########################

# exit game

# get font size
def get_font(size):
    return pygame.font.Font("font.ttf", size)

# return to menu

# shuffling loop (for user guide)

# replay game

# shuffling logic

# shuffling animations (for game)

# reveal marble



########################
### VARIABLE PRESETS ###
########################

# initialize pygame
pygame.init()
# get resolution
user_screen = pygame.display.Info()
print(user_screen.current_w,"x",user_screen.current_h)
# create game screen
SCREEN = pygame.display.set_mode((user_screen.current_w, user_screen.current_h))
# create clock
clock = pygame.time.Clock()
# create game loop boolean
game_running = True
menu_running = True
guide_running = False
play_running = False
# create image variables
BG = pygame.image.load("Background.jpeg")
marble = pygame.image.load("marble.png")
cup = pygame.image.load('cup.png')
cup_small = pygame.transform.scale(cup, (150, 150))
# create audio variables
vine = pygame.mixer.Sound("vine.wav")
ack = pygame.mixer.Sound("ack.wav")
button = pygame.mixer.Sound("menu-button.wav")
# create buttons
PLAY_BUTTON = Button(image=None, pos=(0.5 * user_screen.current_w, 0.4 * user_screen.current_h), 
                            text_input="PLAY!", font=get_font(75), base_color="#FFFFFF", hovering_color="Green")
GUIDE_BUTTON = Button(image=None, pos=(0.5 * user_screen.current_w, 0.6 * user_screen.current_h), 
                            text_input="USER GUIDE", font=get_font(75), base_color="#FFFFFF", hovering_color="Green")
QUIT_BUTTON = Button(image=None, pos=(0.5 * user_screen.current_w, 0.8 * user_screen.current_h), 
                            text_input="QUIT", font=get_font(75), base_color="#FFFFFF", hovering_color="Green")
# create texts
MENU_TEXT = get_font(100).render("SHELLSHOCK", True, "#FFFFFF")

# create misc
MENU_RECT = MENU_TEXT.get_rect(center=(0.5 * user_screen.current_w, 0.15 * user_screen.current_h))
MENU_MOUSE_POS = pygame.mouse.get_pos()

############
### MENU ###
############
def main_menu():
    SCREEN.blit(BG, (0, 0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    for button in [PLAY_BUTTON, GUIDE_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(SCREEN)
    
    pygame.display.flip()
# display game icon

# display game title

# display buttons (play, guide, quit)



##################
### USER GUIDE ###
##################
def guide():
    pass
# display text instructions

# display looping shuffling animation

# display button (return to menu)



############
### PLAY ###
############
def play():
    pass
# display button (return to menu)

# display images (3 shells/cups)

# display image (marble)

# display text (score)

# display text (streak)

# display text (shuffle ready or not)

# display button (shuffle)

# display text (choose)

######################
### EVENT HANDLING ###
######################
def handle_event():
    SCREEN.blit(MENU_TEXT, MENU_RECT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse clicked")
            # if interacting with any button
            #button.play()
            # if failed to guess in game
            vine.play()
            if menu_running == True:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    marble.set_alpha(255)
                    play()
                elif GUIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    guide()
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

#################
### GAME LOOP ###
#################

while game_running:
    handle_event()
    if menu_running == True:
        main_menu()
            
pygame.quit()