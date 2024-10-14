# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DUC PHAM
# Section:      518
# Assignment:   Module 8 team lab (individual component)
# Date:         13-10-2024
#

def char_convert(val,char,key):
    for row_n in range(len(val)): # 0 to 4 inclusive
        #print(val[row_n]) # should print 5 lists with 1 string each
        val[row_n][0] = val[row_n][0].replace(key,char) # replaces key with char
    return val

#Townsend's board
board = []

### formating ###
#integers#
#0
zero = [["000"],
        ["0 0"],
        ["0 0"],
        ["0 0"],
        ["000"]]
#1
one =  [[" 1 "],
        ["11 "],
        [" 1 "],
        [" 1 "],
        ["111"]]
#2
two =  [["222"],
        ["  2"],
        ["222"],
        ["2  "],
        ["222"]]
#3
three =[["333"],
        ["  3"],
        ["333"],
        ["  3"],
        ["333"]]
#4
four = [["4 4"],
        ["4 4"],
        ["444"],
        ["  4"],
        ["  4"]]
#5
five = [["555"],
        ["5  "],
        ["555"],
        ["  5"],
        ["555"]]
#6
six =  [["666"],
        ["6  "],
        ["666"],
        ["6 6"],
        ["666"]]
#7
seven =[["777"],
        ["  7"],
        ["  7"],
        ["  7"],
        ["  7"]]
#8
eight =[["888"],
        ["8 8"],
        ["888"],
        ["8 8"],
        ["888"]]
#9
nine = [["999"],
        ["9 9"],
        ["999"],
        ["  9"],
        ["999"]]

#meridians#
#AM
am =   [[" A  M   M"],
        ["A A MM MM"],
        ["AAA M M M"],
        ["A A M   M"],
        ["A A M   M"]]
#PM
pm =   [["PPP M   M"],
        ["P P MM MM"],
        ["PPP M M M"],
        ["P   M   M"],
        ["P   M   M"]]

#colon
#:
colon = [[" "],
         [":"],
         [" "],
         [":"],
         [" "]] 

#space
# 
space = [[" "],
         [" "],
         [" "],
         [" "],
         [" "]]

mat_clock = {0:zero,
             1:one,
             2:two,
             3:three,
             4:four,
             5:five,
             6:six,
             7:seven,
             8:eight,
             9:nine,
             "am":am,
             "pm":pm,
             ":":colon,
             " ":space}
