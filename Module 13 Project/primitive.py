import os
import time
import sys

import pygame
from pygame import mixer

t_sleep = 0.18
score = 0
pygame.init()
mixer.init
vine = pygame.mixer.Sound("vine.wav")
ack = pygame.mixer.Sound("ack.wav")
button = pygame.mixer.Sound("menu-button.wav")

def ready_shuffle():
    user_input = input("shuffle? [input <enter> to begin]")
    os.system('clear')
    # call respective starting animation

######################
### animation left ###
######################
def animation_ltr_cw():
    motion_ltr_cw =["     \n ooo \n     ",
                    " o   \n  o  \n   o ",
                    "  o  \n  o  \n  o  ",
                    "   o \n  o  \n o   ",
                    "     \n ooo \n     ",]

    for i in motion_ltr_cw:
        print(i)
        time.sleep(t_sleep)
        os.system('clear')

def animation_ltr_cc():
    motion_ltr_cc =["     \n ooo \n     ",
                    "   o \n  o  \n o   ",
                    "  o  \n  o  \n  o  ",
                    " o   \n  o  \n   o ",
                    "     \n ooo \n     ",]

    for i in motion_ltr_cc:
        print(i)
        time.sleep(t_sleep)
        os.system('clear')

def animation_ltm_cw():
    motion_ltm_cw =["     \n ooo \n     ",
                    " o   \n   o \n  o  ",
                    "  o  \n   o \n o   ",
                    "     \n ooo \n     ",]
    
    for i in motion_ltm_cw:
        print(i)
        time.sleep(t_sleep)
        os.system('clear')

def animation_ltm_cc():
    motion_ltm_cc =["     \n ooo \n     ",
                    "  o  \n   o \n o   ",
                    " o   \n   o \n  o  ",
                    "     \n ooo \n     ",]
    
    for i in motion_ltm_cc:
        print(i)
        time.sleep(t_sleep)
        os.system('clear') 

#######################
### animation right ###
#######################
def animation_rtl_cw():
    animation_ltr_cc()

def animation_rtl_cc():
    animation_ltr_cw()

def animation_rtm_cw():
    motion_rtm_cw =["     \n ooo \n     ",
                    "   o \n o   \n o   ",
                    "  o  \n o   \n  o  ",
                    "     \n ooo \n     ",]
    for i in motion_rtm_cw:
        print(i)
        time.sleep(t_sleep)
        os.system('clear')

def animation_rtm_cc():
    motion_rtm_cc =["     \n ooo \n     ",
                    "  o  \n o   \n   o ",
                    "   o \n o   \n  o  ",
                    "     \n ooo \n     ",]
    for i in motion_rtm_cc:
        print(i)
        time.sleep(t_sleep)
        os.system('clear')

########################
### animation middle ###
########################
def animation_mtl_cw():
    animation_ltm_cc()

def animation_mtl_cc():
    animation_ltm_cw()

def animation_mtr_cw():
    animation_rtm_cc()

def animation_mtr_cc():
    animation_rtm_cw()

import random

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
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[0] = False
    arr[2] = True
    animation_ltr_cw()
    
    shuffle_int = random.randint(9,12)
    if shuffle_int == 9:
        rtl_cw(arr,total)
    elif shuffle_int == 10:
        rtl_cc(arr,total)
    elif shuffle_int == 11:
        rtm_cw(arr, total)
    elif shuffle_int == 12:
        rtm_cc(arr, total)
    return None

def ltr_cc(arr,total):
    '''
    move marble left to right, counterclockwise

    Returns
    -------
    None.

    '''
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[0] = False
    arr[2] = True
    animation_ltr_cc()
    
    shuffle_int = random.randint(9,12)
    if shuffle_int == 9:
        rtl_cw(arr,total)
    elif shuffle_int == 10:
        rtl_cc(arr,total)
    elif shuffle_int == 11:
        rtm_cw(arr, total)
    elif shuffle_int == 12:
        rtm_cc(arr, total)
    return None

def ltm_cw(arr,total):
    '''
    mover marble left to middle, clockwise

    Returns
    -------
    None.

    '''
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[0] = False
    arr[1] = True
    animation_ltm_cw()
    
    shuffle_int = random.randint(5,8)
    
    if shuffle_int == 5:
        mtr_cw(arr,total)
    elif shuffle_int == 6:
        mtr_cc(arr,total)
    elif shuffle_int == 7:
        mtl_cw(arr, total)
    elif shuffle_int == 8:
        mtl_cc(arr, total)
    return None

def ltm_cc(arr,total):
    '''
    mover marble left to middle, counterclockwise

    Returns
    -------
    None.

    '''
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[0] = False
    arr[1] = True
    animation_ltm_cc()
    
    shuffle_int = random.randint(5,8)
    
    if shuffle_int == 5:
        mtr_cw(arr,total)
    elif shuffle_int == 6:
        mtr_cc(arr,total)
    elif shuffle_int == 7:
        mtl_cw(arr, total)
    elif shuffle_int == 8:
        mtl_cc(arr, total)
    return None

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
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[1] = False
    arr[2] = True
    animation_mtr_cw()
    
    shuffle_int = random.randint(9,12)
    if shuffle_int == 9:
        rtl_cw(arr,total)
    elif shuffle_int == 10:
        rtl_cc(arr,total)
    elif shuffle_int == 11:
        rtm_cw(arr, total)
    elif shuffle_int == 12:
        rtm_cc(arr, total)
    return None

def mtr_cc(arr,total):
    '''
    move marble middle to right, counterclockwise

    Returns
    -------
    None.

    '''
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[1] = False
    arr[2] = True
    animation_mtr_cc()
    
    shuffle_int = random.randint(9,12)
    if shuffle_int == 9:
        rtl_cw(arr,total)
    elif shuffle_int == 10:
        rtl_cc(arr,total)
    elif shuffle_int == 11:
        rtm_cw(arr, total)
    elif shuffle_int == 12:
        rtm_cc(arr, total)
    return None

def mtl_cw(arr,total):
    '''
    move marble middle to left, clockwise

    Returns
    -------
    None.

    '''
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[1] = False
    arr[0] = True
    animation_mtl_cw()
    
    shuffle_int = random.randint(1,4)# initial shuffle randomly generated by computer
    
    if shuffle_int == 1:
        ltr_cw(arr,total)
    elif shuffle_int == 2:
        ltr_cc(arr,total)
    elif shuffle_int == 3:
        ltm_cw(arr, total)
    elif shuffle_int == 4:
        ltm_cc(arr, total)
    return None

def mtl_cc(arr,total):
    '''
    move marble middle to left, counterclockwise

    Returns
    -------
    None.

    '''
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[1] = False
    arr[0] = True
    animation_mtl_cc()
    
    shuffle_int = random.randint(1,4)# initial shuffle randomly generated by computer
    
    if shuffle_int == 1:
        ltr_cw(arr,total)
    elif shuffle_int == 2:
        ltr_cc(arr,total)
    elif shuffle_int == 3:
        ltm_cw(arr, total)
    elif shuffle_int == 4:
        ltm_cc(arr, total)
    return None

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
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[2] = False
    arr[0] = True
    animation_rtl_cw()
    
    shuffle_int = random.randint(1,4)# initial shuffle randomly generated by computer
    
    if shuffle_int == 1:
        ltr_cw(arr,total)
    elif shuffle_int == 2:
        ltr_cc(arr,total)
    elif shuffle_int == 3:
        ltm_cw(arr, total)
    elif shuffle_int == 4:
        ltm_cc(arr, total)
    return None

def rtl_cc(arr,total):
    '''
    move marble right to left, counterclockwise

    Returns
    -------
    None.

    '''
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[2] = False
    arr[0] = True
    animation_rtl_cc()
    
    shuffle_int = random.randint(1,4)# initial shuffle randomly generated by computer
    
    if shuffle_int == 1:
        ltr_cw(arr,total)
    elif shuffle_int == 2:
        ltr_cc(arr,total)
    elif shuffle_int == 3:
        ltm_cw(arr, total)
    elif shuffle_int == 4:
        ltm_cc(arr, total)
    return None

def rtm_cw(arr,total):
    '''
    move marble right to middle, clockwise

    Returns
    -------
    None.

    '''
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None
    
    # swap!
    arr[2] = False
    arr[1] = True
    animation_rtm_cw()
    
    shuffle_int = random.randint(5,8)
    
    if shuffle_int == 5:
        mtr_cw(arr,total)
    elif shuffle_int == 6:
        mtr_cc(arr,total)
    elif shuffle_int == 7:
        mtl_cw(arr, total)
    elif shuffle_int == 8:
        mtl_cc(arr, total)
    return None

def rtm_cc(arr,total):
    '''
    move marble right to middle, counterclockwise

    Returns
    -------
    None.

    '''
    total -= 1
    
    if total == 0:
        guess_marble(arr)
        return None

    arr[2] = False
    arr[1] = True
    animation_rtm_cc()
    
    shuffle_int = random.randint(5,8)
    
    if shuffle_int == 5:
        mtr_cw(arr,total)
    elif shuffle_int == 6:
        mtr_cc(arr,total)
    elif shuffle_int == 7:
        mtl_cw(arr, total)
    elif shuffle_int == 8:
        mtl_cc(arr, total)
    return None

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
        print("arrangement (True is where the marble belong):\n",arrangement)
        shuffle_int = random.randint(1,4)# initial shuffle randomly generated by computer
        
        ready_shuffle()

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
        print("arrangement (True is where the marble belong):\n",arrangement)
        shuffle_int = random.randint(5,8)
        
        ready_shuffle()

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
        print("arrangement (True is where the marble belong):\n",arrangement)
        shuffle_int = random.randint(9,12)

        ready_shuffle()

        if shuffle_int == 9:
            rtl_cw(arrangement,pm_s_total)
        elif shuffle_int == 10:
            rtl_cc(arrangement,pm_s_total)
        elif shuffle_int == 11:
            rtm_cw(arrangement, pm_s_total)
        elif shuffle_int == 12:
            rtm_cc(arrangement, pm_s_total)

def play():
    os.system('clear') # clean up screen
    difficulty = 1 # use to scale various dynamics of the game

    # get the index of the box the player choose
    # enable mouse input # saved as user text input for now [0,1,2]

    arrangement = [None, None, None] # set up of the three shells
    initial_m_index = random.randint(0, 2) #input("pick the box you want to place the marble in: ")
    shuffle_total   = random.randint(1, difficulty*6+1) # random total of time we are shuffling

    print("inital marble placement",initial_m_index)
    #print("total # shuffle",shuffle_total)

    place_marble(initial_m_index, shuffle_total)

def view_score(): # work in progress
    print(f"your score is {score}")
    while True:
        user_input = input("Would you like to play again [y/n]?")
        if user_input == "y":
            play()
            break
        elif user_input == "n":
            menu()
            break
        else:
            print("Invalid input. Enter again")
            user_input = input("Would you like to play again [y/n]?")

def play_again():
    while True:
        user_input = input("Would you like to play again [y/n]?")
        if user_input == "y":
            play()
            break
        elif user_input == "n":
            user_input = input("Would you like see your score [y/n]?")
            while True:
                if user_input == "y":
                    view_score()
                    break
                elif user_input == "n":
                    menu()
                    break
            break
        else:
            print("Invalid input. Enter again")
            user_input = input("Would you like to play again [y/n]?")

def guess_marble(arr):
    print("     \n ooo \n     ") # reset position
    #print(arr) # temporarily cheat in our game to confirm results
    user_guess = input("Your guess [0,1,2] --> ")
    if arr[int(user_guess)] == True:
        print("congrats!")
        play_again()
    else:
        vine.play()
        print("bruh")
        time.sleep(2)
        play_again()
    # if not a valid input, loop try again

    return None

def manual():
    user_return = input("press <enter> to return to the menu")
    while True:
        if user_return == '':
            menu()
            break
        else:
            print("invalid input")
            user_return = input("press <enter> to return to the menu")

def quit():
    os.system('clear')
    last_text = "good bye"
    t_bye = 0.5
    for i in range(1,len(last_text)):
        time.sleep(t_bye/i)
        print(last_text)
        time.sleep(t_bye/i)
        os.system('clear')
    sys.exit()

def menu():
    os.system('clear') # clean up screen
    acceptable_input = {"1":"playing game!","2":"loading manual...","3":"until next time"} # dictionary use case!
    game_banner = "---<<< S H E L L  S H O C K >>>---"
    game_directories = [("1 - PLAY").center(len(game_banner)),
                        ("2 - MANUAL").center(len(game_banner)),
                        ("3 - QUIT").center(len(game_banner))]

    print(game_banner+"\n")
    for i in game_directories:
        print(i)
    print()
    user_directory = input("Where would you like to go? ")

    # try-except use case
    while True:
        try:
            print(acceptable_input[user_directory])
            break
        except KeyError:
            print(f"\"{user_directory}\" is not a valid directory. Please enter a valid directory")
            user_directory = input("Where would you like to go? ")

    # use case of if-elif chain"
    if user_directory ==  "1":
        button.play()
        play()
    elif user_directory == "2":
        button.play()
        manual()
    elif user_directory == "3":
        ack.play()
        quit()
menu()
