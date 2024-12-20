# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names:
# Townsend Wheeler
# Duc Pham
# Archelaus Paxon
# Julian Curry
# Section: 518
# Assignment: Lab Topic 13 Team Project
# Date: 19-11-2024

import pygame, sys
from button import Button
import random
from rtl_animation_ccw import rtl_animation_ccw
from rtl_animation_ccw import rtl_animation_ccw_reset
from ctr_animation_ccw import ctr_animation_ccw
from ctr_animation_ccw import ctr_animation_ccw_reset
from ctl_animation_ccw import ctl_animation_ccw
from ctl_animation_ccw import ctl_animation_ccw_reset
from rtl_animation_cw import rtl_animation_cw
from rtl_animation_cw import rtl_animation_cw_reset
from ctr_animation_cw import ctr_animation_cw
from ctr_animation_cw import ctr_animation_cw_reset
from ctl_animation_cw import ctl_animation_cw
from ctl_animation_cw import ctl_animation_cw_reset

pygame.init()

vine = pygame.mixer.Sound("vine.wav")
button_sound = pygame.mixer.Sound("menu-button.wav")


try:
    cup = pygame.image.load('cup.png')
except:
    print('Error loading the image. Make sure the cup png is downloaded')
cup_small = pygame.transform.scale(cup, (150, 150))
a, b, cup_x, cup_y = cup_small.get_rect()
the_tuple = a, b, cup_x, cup_y

animation_dict = {}
reset_dict = {}
def guess_marble(arr):
    return None
#################################
### marble starts at left box ###
#################################

def ltr_cw(arr,total):
    '''
    move marble left to right, clockwise

    Returns
    -------
    None.

    '''
    global animation_dict
    global reset_dict
    animation_dict['rtlcw1'] = rtl_animation_cw
    reset_dict['rtlcw_reset1'] = rtl_animation_cw_reset
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[0] = False
    arr[2] = True
    
    
    shuffle_int = random.randint(9,12)
    if shuffle_int == 9:
        rtl_cw(arr,total)
    elif shuffle_int == 10:
        rtl_cc(arr,total)
    elif shuffle_int == 11:
        rtm_cw(arr, total)
    elif shuffle_int == 12:
        rtm_cc(arr, total)
        
    # call designated visual function
    return arr

def ltr_cc(arr,total):
    '''
    move marble left to right, counterclockwise

    Returns
    -------
    None.

    '''
    global animation_dict
    global reset_dict
    animation_dict['rtlccw_1'] = rtl_animation_ccw
    reset_dict['rtlccw_reset_1'] = rtl_animation_ccw_reset
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[0] = False
    arr[2] = True

    
    shuffle_int = random.randint(9,12)
    if shuffle_int == 9:
        rtl_cw(arr,total)
    elif shuffle_int == 10:
        rtl_cc(arr,total)
    elif shuffle_int == 11:
        rtm_cw(arr, total)
    elif shuffle_int == 12:
        rtm_cc(arr, total)
        
    # call designated visual function
    return arr

def ltm_cw(arr,total):
    '''
    mover marble left to middle, clockwise

    Returns
    -------
    None.

    '''
    global animation_dict
    global reset_dict
    animation_dict['ctlcw1'] = ctl_animation_cw
    reset_dict['ctlcw_reset1'] = ctl_animation_cw_reset
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[0] = False
    arr[1] = True
    
    shuffle_int = random.randint(5,8)
    
    if shuffle_int == 5:
        mtr_cw(arr,total)
    elif shuffle_int == 6:
        mtr_cc(arr,total)
    elif shuffle_int == 7:
        mtl_cw(arr, total)
    elif shuffle_int == 8:
        mtl_cc(arr, total)
    
    # call designated visual function
    return arr

def ltm_cc(arr,total):
    '''
    mover marble left to middle, counterclockwise

    Returns
    -------
    None.

    '''
    global animation_dict
    global reser_dict
    animation_dict['ctlccw1'] = ctl_animation_ccw
    reset_dict['ctlccw_reset1'] = ctl_animation_ccw_reset    
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[0] = False
    arr[1] = True
    
    shuffle_int = random.randint(5,8)
    
    if shuffle_int == 5:
        mtr_cw(arr,total)
    elif shuffle_int == 6:
        mtr_cc(arr,total)
    elif shuffle_int == 7:
        mtl_cw(arr, total)
    elif shuffle_int == 8:
        mtl_cc(arr, total)
    
    # call designated visual function
    return arr

###################################
### marble starts at middle box ###
###################################

def mtr_cw(arr,total):
    '''
    move marble middle to right, clockwise

    Returns
    -------
    None.

    '''
    global animation_dict
    global reset_dict
    animation_dict['ctrcw1'] = ctr_animation_cw
    reset_dict['ctrcw_reset1'] = ctr_animation_cw_reset  
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[1] = False
    arr[2] = True

    
    shuffle_int = random.randint(9,12)
    if shuffle_int == 9:
        rtl_cw(arr,total)
    elif shuffle_int == 10:
        rtl_cc(arr,total)
    elif shuffle_int == 11:
        rtm_cw(arr, total)
    elif shuffle_int == 12:
        rtm_cc(arr, total)
        
    # call designated visual function
    return arr

def mtr_cc(arr,total):
    '''
    move marble middle to right, counterclockwise

    Returns
    -------
    None.

    '''
    global animation_dict
    global reset_dict
    animation_dict['ctrccw1'] = ctr_animation_ccw
    reset_dict['ctrccw_reset1'] = ctr_animation_ccw_reset
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[1] = False
    arr[2] = True
    
    shuffle_int = random.randint(9,12)
    if shuffle_int == 9:
        rtl_cw(arr,total)
    elif shuffle_int == 10:
        rtl_cc(arr,total)
    elif shuffle_int == 11:
        rtm_cw(arr, total)
    elif shuffle_int == 12:
        rtm_cc(arr, total)
        
    # call designated visual function
    return None

def mtl_cw(arr,total):
    '''
    move marble middle to left, clockwise

    Returns
    -------
    None.

    '''
    global animation_dict
    global reset_dict
    animation_dict['ctlcw2'] = ctl_animation_cw
    reset_dict['ctlcw_reset'] = ctl_animation_cw_reset  
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[1] = False
    arr[0] = True

    
    shuffle_int = random.randint(1,4)# initial shuffle randomly generated by computer
    
    if shuffle_int == 1:
        ltr_cw(arr,total)
    elif shuffle_int == 2:
        ltr_cc(arr,total)
    elif shuffle_int == 3:
        ltm_cw(arr, total)
    elif shuffle_int == 4:
        ltm_cc(arr, total)
    
    # call designated visual function
    return arr

def mtl_cc(arr,total):
    '''
    move marble middle to left, counterclockwise

    Returns
    -------
    None.

    '''
    global animation_dict
    global reset_dict

    animation_dict['ctlccw2'] = ctl_animation_ccw
    reset_dict['ctlccw_reset'] = ctl_animation_ccw_reset
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[1] = False
    arr[0] = True

    
    shuffle_int = random.randint(1,4)# initial shuffle randomly generated by computer
    
    if shuffle_int == 1:
        ltr_cw(arr,total)
    elif shuffle_int == 2:
        ltr_cc(arr,total)
    elif shuffle_int == 3:
        ltm_cw(arr, total)
    elif shuffle_int == 4:
        ltm_cc(arr, total)
    
    # call designated visual function
    return arr

##################################
### marble starts at right box ###
##################################

def rtl_cw(arr,total):
    '''
    move marble right to left, clockwise

    Returns
    -------
    None.

    '''
    global animation_dict
    global reset_dict
    animation_dict['rtlcw2'] = rtl_animation_cw
    reset_dict['rtlcw_reset2'] = rtl_animation_cw_reset
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[2] = False
    arr[0] = True

    
    shuffle_int = random.randint(1,4)# initial shuffle randomly generated by computer
    
    if shuffle_int == 1:
        ltr_cw(arr,total)
    elif shuffle_int == 2:
        ltr_cc(arr,total)
    elif shuffle_int == 3:
        ltm_cw(arr, total)
    elif shuffle_int == 4:
        ltm_cc(arr, total)
    
    # call designated visual function
    return arr

def rtl_cc(arr,total):
    '''
    move marble right to left, counterclockwise

    Returns
    -------
    None.

    '''
    global animation_dict
    global reset_dict
    animation_dict['rtlccw2'] = rtl_animation_ccw
    reset_dict['rtlccw_reset2'] = rtl_animation_ccw_reset
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[2] = False
    arr[0] = True
    
    shuffle_int = random.randint(1,4)# initial shuffle randomly generated by computer
    
    if shuffle_int == 1:
        ltr_cw(arr,total)
    elif shuffle_int == 2:
        ltr_cc(arr,total)
    elif shuffle_int == 3:
        ltm_cw(arr, total)
    elif shuffle_int == 4:
        ltm_cc(arr, total)
    
    # call designated visual function
    return arr

def rtm_cw(arr,total):
    '''
    move marble right to middle, clockwise

    Returns
    -------
    None.

    '''
    global animation_dict
    global reset_dict
    animation_dict['ctrcw2'] = ctr_animation_cw
    reset_dict['ctrcw_reset2'] = ctr_animation_cw_reset  
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[2] = False
    arr[1] = True
    
    shuffle_int = random.randint(5,8)
    
    if shuffle_int == 5:
        mtr_cw(arr,total)
    elif shuffle_int == 6:
        mtr_cc(arr,total)
    elif shuffle_int == 7:
        mtl_cw(arr, total)
    elif shuffle_int == 8:
        mtl_cc(arr, total)
    
    # call designated visual function
    return arr

def rtm_cc(arr,total):
    '''
    move marble right to middle, counterclockwise

    Returns
    -------
    None.

    '''
    global animatino_dict
    global reset_dict
    animation_dict['ctrccw'] = ctr_animation_ccw
    reset_dict['ctrccw_reset'] = ctr_animation_ccw_reset
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None

    arr[2] = False
    arr[1] = True
    
    shuffle_int = random.randint(5,8)
    
    if shuffle_int == 5:
        mtr_cw(arr,total)
    elif shuffle_int == 6:
        mtr_cc(arr,total)
    elif shuffle_int == 7:
        mtl_cw(arr, total)
    elif shuffle_int == 8:
        mtl_cc(arr, total)
    
    # call designated visual function
    return arr

##########################################

def place_marble(pm_i_m_index,pm_s_total):
    '''
    initialize by the player once per round.
    call the first random logical shuffle sequence.

    Returns
    -------
    arrangement : list
        current arrangement of the shells (containing and not containing marble)

    '''

    if pm_i_m_index == 0: # player place marble in left shell

        arrangement = [True, False, False]
        shuffle_int = random.randint(1,4)# initial shuffle randomly generated by computer
        
        if shuffle_int == 1:
            ltr_cw(arrangement,pm_s_total)
        elif shuffle_int == 2:
            ltr_cc(arrangement,pm_s_total)
        elif shuffle_int == 3:
            ltm_cw(arrangement, pm_s_total)
        elif shuffle_int == 4:
            ltm_cc(arrangement, pm_s_total)
                
    elif pm_i_m_index == 1:
        arrangement = [False, True, False]
        shuffle_int = random.randint(5,8)
        
        if shuffle_int == 5:
            mtr_cw(arrangement,pm_s_total)
        elif shuffle_int == 6:
            mtr_cc(arrangement,pm_s_total)
        elif shuffle_int == 7:
            mtl_cw(arrangement, pm_s_total)
        elif shuffle_int == 8:
            mtl_cc(arrangement, pm_s_total)
        
    elif pm_i_m_index == 2:
        arrangement = [False, False, True]
        shuffle_int = random.randint(9,12)

        if shuffle_int == 9:
            rtl_cw(arrangement,pm_s_total)
        elif shuffle_int == 10:
            rtl_cc(arrangement,pm_s_total)
        elif shuffle_int == 11:
            rtm_cw(arrangement, pm_s_total)
        elif shuffle_int == 12:
            rtm_cc(arrangement, pm_s_total)
    return arrangement





### variable presets ###


# get the index of the box the player choose
# enable mouse input # saved as user text input for now [0,1,2]

arrangement = [None, None, None] # set up of the three shells
initial_m_index = 1 
shuffle_total   = 5 # random total of time we are shuffling

final_arrangment = place_marble(initial_m_index, shuffle_total)


print(final_arrangment)

### THIS IS THE GAME LOOP SECTION ###

# SET ALL THE REQUIRED PYGAME VARIABLES 
import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720)) #This is the screen size! 1280 by 720
pygame.display.set_caption("Menu")
try:
    BG = pygame.image.load("Background.jpg")
except:
    print('Error in loading the background. Make sure it is downloaded and placed in the same directory')

clock = pygame.time.Clock()

def get_font(size):
    try:
        return pygame.font.Font("font.ttf", size)
    except:
        print("You don't have the font downloaed")
        return None
## SET THE TIMING VARIABLES##
print(animation_dict)
animation_values = list(animation_dict.values())
reset_values = list(reset_dict.values())
print(animation_values)
timer1 = 0
timer2 = 0
timer3 = 0
timer4 = 0
timer5 = 0
timer6 = 0
timer7 = 0
timer8 = 0
timer9 = 0
reset_count = 0
##THIS IS THE GAME LOOP##
def play():
    global timer1
    global timer2
    global timer3
    global timer4
    global timer5
    global timer6
    global timer7
    global timer8
    global timer9
    global reset_count
    global animation_values
    global reset_values
    global cup_small
    global the_tuple
    global final_arrangment

    while True:
        clock.tick(60)
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        if timer1 < 301:
            PLAY_TEXT = get_font(20).render("There was a marble placed in the center cup. Keep track of it!!!", True, "Black")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50)) 
            SCREEN.blit(PLAY_TEXT, PLAY_RECT)#Puts "This is the GAME screen." on the top and center of the screen
            timer1 += 1
        elif timer2 < 28:
            for i in range(len(animation_values)):
                animation_values[i]()
                break
            timer2 += 1
        elif reset_count == 0:
            for i in range(len(reset_values)):
                reset_values[i]()
                reset_count += 1
                break
       
        elif timer3 < 28:
            for i in range(len(animation_values)):
                animation_values[i+1]()
                break
            timer3 += 1
        elif reset_count == 1:
            for i in range(len(reset_values)):
                reset_values[i+1]()
                reset_count += 1
                break
        elif timer4 < 28:
            for i in range(len(animation_values)):
                animation_values[i+2]()
                break
            timer4 += 1
        elif reset_count == 2:
            for i in range(len(reset_values)):
                reset_values[i+2]()
                reset_count += 1
                break
        elif timer5 < 28:
            for i in range(len(animation_values)):
                animation_values[i+3]()
                break
            timer5 += 1
        elif reset_count == 3:
            for i in range(len(reset_values)):
                reset_values[i+3]()
                reset_count += 1
                break
        elif timer6 < 28:
            for i in range(len(animation_values)):
                animation_values[i+4]()
                break
            timer6 += 1
        elif reset_count == 4:
            for i in range(len(reset_values)):
                reset_values[i+4]()
                reset_count += 1
                break
        elif timer7 < 200:
            PLAY_TEXT = get_font(20).render("Which cup is the marble in?", True, "Black")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50)) 
            SCREEN.blit(PLAY_TEXT, PLAY_RECT)#Puts "This is the GAME screen." on the top and center of the screen
            SCREEN.blit(cup_small, ((SCREEN.get_width())/3-the_tuple[2]/2, (SCREEN.get_height())/2-the_tuple[3]/2))
            SCREEN.blit(cup_small, (SCREEN.get_width()/2-the_tuple[2]/2, SCREEN.get_height()/2-the_tuple[3]/2))
            SCREEN.blit(cup_small, (SCREEN.get_width()/3*2-the_tuple[2]/2, SCREEN.get_height()/2-the_tuple[3]/2))
            timer7 +=1
        elif timer8 < 200:
            if final_arrangment[0]:
                PLAY_TEXT = get_font(20).render("The Marble was in the first cup!!!", True, "Black")
                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50)) 
                SCREEN.blit(PLAY_TEXT, PLAY_RECT)#Puts "This is the GAME screen." on the top and center of the screen
            if final_arrangment[1]:
                PLAY_TEXT = get_font(20).render("The Marble was in the second cup!!!", True, "Black")
                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50)) 
                SCREEN.blit(PLAY_TEXT, PLAY_RECT)#Puts "This is the GAME screen." on the top and center of the screen
            if final_arrangment[2]:
                PLAY_TEXT = get_font(20).render("The Marble was in the third cup!!!", True, "Black")
                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50)) 
                SCREEN.blit(PLAY_TEXT, PLAY_RECT)#Puts "This is the GAME screen." on the top and center of the screen
            timer8 += 1
        else:
            PLAY_TEXT = get_font(20).render("Thanks for playing !!!", True, "Black")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50)) 
            SCREEN.blit(PLAY_TEXT, PLAY_RECT)#Puts "This is the GAME screen." on the top and center of the screen
        




        
        
        PLAY_BACK = Button(image=None, pos=(1125, 670), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                button_sound.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    button_sound.play()
                    main_menu()

        pygame.display.update()
    
def guide():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        GUIDE_TEXT = get_font(35).render("This is the USER GUIDE.", True, "Black")
        GUIDE_RECT = GUIDE_TEXT.get_rect(center=(320, 150))
        SCREEN.blit(GUIDE_TEXT, GUIDE_RECT)
        
        GUIDE_TEXT2 = get_font(35).render("1) Put a marble in any of the three boxes.", True, "Black")
        GUIDE_RECT2 = GUIDE_TEXT.get_rect(center=(320, 200))
        SCREEN.blit(GUIDE_TEXT2, GUIDE_RECT2)
        
        GUIDE_TEXT3 = get_font(35).render("2) The boxes will shuffle randomly.", True, "Black")
        GUIDE_RECT3 = GUIDE_TEXT.get_rect(center=(320, 250))
        SCREEN.blit(GUIDE_TEXT3, GUIDE_RECT3)
        
        GUIDE_TEXT4 = get_font(35).render("3) You will guess the box the marble is in.", True, "Black")
        GUIDE_RECT4 = GUIDE_TEXT.get_rect(center=(320, 300))
        SCREEN.blit(GUIDE_TEXT4, GUIDE_RECT4)
        
        GUIDE_TEXT4 = get_font(35).render("    The correct answer will be revealed after you", True, "Black")
        GUIDE_RECT4 = GUIDE_TEXT.get_rect(center=(320,350))
        SCREEN.blit(GUIDE_TEXT4, GUIDE_RECT4)
        
        GUIDE_TEXT5 = get_font(35).render("    click on a cup.", True, "Black")
        GUIDE_RECT5 = GUIDE_TEXT.get_rect(center=(320,400))
        SCREEN.blit(GUIDE_TEXT5, GUIDE_RECT5)
        
        GUIDE_TEXT6 = get_font(35).render("4) Once finished, press BACK to return to ", True, "Black")
        GUIDE_RECT6 = GUIDE_TEXT.get_rect(center=(320,450))
        SCREEN.blit(GUIDE_TEXT6, GUIDE_RECT6)
        
        GUIDE_TEXT7 = get_font(35).render("    the main screen and press QUIT to exit.", True, "Black")
        GUIDE_RECT7 = GUIDE_TEXT.get_rect(center=(320, 500))
        SCREEN.blit(GUIDE_TEXT7, GUIDE_RECT7)

        GUIDE_BACK = Button(image=None, pos=(1125, 670), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        GUIDE_BACK.changeColor(OPTIONS_MOUSE_POS)
        GUIDE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                button_sound.play()
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
                    button_sound.play()
                    play()
                elif GUIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    button_sound.play()
                    guide()
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    button_sound.play
                    pygame.quit()
                    sys.exit()
                else:
                    vine.play()

        pygame.display.update()

main_menu()