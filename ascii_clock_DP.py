#board
board = [[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "], 
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "], 
         [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]

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
'''
for r in mat_clock[":"]:
    for c in r:
        print(c)
'''

# first: notice column value of 0
for i in range(len(board)):
    board[i][0] = mat_clock[1][i][0]

# second: notice column value of 3
for i in range(len(board)):
    board[i][3] = mat_clock[2][i][0]
    

# third: notice column value of 4
for i in range(len(board)):
    board[i][4] = mat_clock[" "][i][0]

# fourth: notice column value of 5
for i in range(len(board)):
    board[i][5] = mat_clock[":"][i][0]
    
# fifth: notice column value of 6
for i in range(len(board)):
    board[i][6] = mat_clock[" "][i][0]

# sixth: notice column value of 8
for i in range(len(board)):
    board[i][8] = mat_clock[3][i][0]

# seventh: notice column value of 11
for i in range(len(board)):
    board[i][11] = mat_clock[0][i][0]

# eighth: notice column value of 12
for i in range(len(board)):
    board[i][14] = mat_clock["pm"][i][0]

### board display ###
for r in board:
    for c in r:
        print(c,end="")
    print()








