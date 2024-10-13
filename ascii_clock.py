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


### input ###
#time
time = input("Enter the time: ")
while ":" not in time: #Check if time has a colon
    time = input("Please enter a colon with the time! Enter the time: ")
time_list = time.split(":")
#Check if the hour is between 0 to 24
while int(time_list[0]) < 0 or int(time_list[0]) > 24:
    time = input("Please enter a valid time1! Enter the time: ")
    time_list = time.split(":")
#check if the minutes is between 0 - 60
while int(time_list[1]) < 0 or int(time_list[1]) > 60:
    time = input("Please enter a valid time2! Enter the time: ")
    time_list = time.split(":")
#Check if first half of time has 1 or 2 digits
while len(time_list[0]) not in [1,2]:
    time = input("Please enter a valid time3! Enter the time: ")
    time_list = time.split(":")
#Check if second half of time has 2 digits
while len(time_list[1]) != 2:
    time = input("Please enter a valid time4! Enter the time: ")
    time_list = time.split(":")
#Store the hour and minutes separately
hour = time_list[0]
minutes = time_list[1]


#format
clock_type = input("Choose the clock type (12 or 24): ")
while clock_type not in ["12", "24"]:
    clock_type = input("Time type not permitted! Try again: ")

#character # Duc modified #
allowed_chars = "abcdeghkmnopqrsuvwxyz@$&*="
fav_char = input("Enter your preferred character: ")
if fav_char == "": # turn into numerical ascii value
    print()
else:
    while fav_char not in allowed_chars or len(fav_char) != 1:
        fav_char = input("Character not permitted! Try again: ")
    print()
    
# make all the number into the char value
if fav_char != "":
    for i in range(10): #0 to 9 inclusive
        mat_clock[i] = char_convert(mat_clock[i], fav_char, str(i))

## 12 hour ##
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
# Assignment: Lab Topic 8
# Date: 13-10-2024

# make if else statement deciding whether or not 12-hours or military clock is desired
# if twelve hours clock is desired find if the hours are less than twelve

#If hours are more than 12, subtract 12 from hours, and update board with time and PM
if clock_type == '12':
    if int(time_list[0])>= 12:
        if int(time_list[0]) == 12: #int compare to int
            time_list[0] = int(time_list[0]) #noon
        elif int(time_list[0]) != 12:
            time_list[0] = int(time_list[0])-12 #afternoon
        if time_list[0] >= 10:
            board.append(mat_clock[int(time_list[0])//10])
            board.append(mat_clock[int(time_list[0])%10])
            board.append(mat_clock[":"])
            board.append(mat_clock[int(time_list[1])//10])
            board.append(mat_clock[int(time_list[1])%10])
            board.append(mat_clock['pm'])
        else:
            board.append(mat_clock[int(time_list[0])])
            board.append(mat_clock[':'])
            board.append(mat_clock[int(time_list[1])//10])
            board.append(mat_clock[int(time_list[1])%10]) 
            board.append(mat_clock['pm'])
#If hours are less than 12, update board to be given time with AM
    else:
        if int(time_list[0]) == 0:#midnight hours
            board.append(mat_clock[1])
            board.append(mat_clock[2])
            board.append(mat_clock[':'])
            board.append(mat_clock[int(time_list[1])//10])
            board.append(mat_clock[int(time_list[1])%10])
            board.append(mat_clock['am']) 
        elif int(time_list[0]) >= 10:
            board.append(mat_clock[int(time_list[0])//10])
            board.append(mat_clock[int(time_list[0])%10])
            board.append(mat_clock[':'])
            board.append(mat_clock[int(time_list[1])//10])
            board.append(mat_clock[int(time_list[1])%10])
            board.append(mat_clock['am']) 
        else:
           board.append(mat_clock[int(time_list[0])])
           board.append(mat_clock[':'])
           board.append(mat_clock[int(time_list[1])//10])
           board.append(mat_clock[int(time_list[1])%10]) 
           board.append(mat_clock['am'])
                
## 24 hours ##
# Make board using matrices using the given time
else:
    if int(time_list[0]) >= 10:
        board.append(mat_clock[int(time_list[0])//10])
        board.append(mat_clock[int(time_list[0])%10])
        board.append(mat_clock[':'])
        board.append(mat_clock[int(time_list[1])//10])
        board.append(mat_clock[int(time_list[1])%10])
    else:
        board.append(mat_clock[int(time_list[0])])
        board.append(mat_clock[':'])
        board.append(mat_clock[int(time_list[1])//10])
        board.append(mat_clock[int(time_list[1])%10])

### TW board display ###
for i in range(len(board[0])):
    for k in range(len(board)):
        if k == len(board)-1:# for the ending to not have extra spaces
            print(board[k][i][0], end="")
        else:
            print(board[k][i][0], end=" ")
    print()
