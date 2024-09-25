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
# Assignment: Lab Topic 7
# Date: 25-9-2024

### WELCOME ###
print("Welcome to Python Go!\n===<*>===")
print("Take turn entering the row and column number of your tile placement")
print("Top left: [1,1]\tBottom right: [9,9]\n")

board = [[".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".",".",".",".",".",".","."]]

turn = False # flip flop b/w True and False
user_row = 1 # first input 
user_column = 1 # second input
in_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #setting list of possible inputs
#Game runs inside one loop, if loop breaks, game ends.
while user_row != "stop" or user_column != "stop": 
    if turn == False:
        user_column = input('Player 1 Choose your desired column:' )
        if user_column == 'stop' or user_row == 'stop':
            break
        user_row = input('Player 1 Choose your desired row:')
        if user_column == 'stop' or user_row == 'stop':
            break
#Making sure that input is in range        
        while user_column not in in_board or user_row not in in_board:
            print("This space isn't on the board, choose a different place!")
            user_column = input('Player 1 Choose your desired column:' )
            if user_column == 'stop' or user_row == 'stop':
                break
            user_row = input('Player 1 Choose your desired row:')
            if user_column == 'stop' or user_row == 'stop':
                break
#Making sure that the input hasn't been used before
        while board[int(user_row)-1][int(user_column)-1] == chr(9675) or board[int(user_row)-1][int(user_column)-1] == chr(9679):
            print('This Space has already been played, choose a different place!')
            user_column = input('Player 1 Choose your desired column:' )
            if user_column == 'stop' or user_row == 'stop':
                break
            user_row = input('Player 1 Choose your desired row:')
            if user_column == 'stop' or user_row == 'stop':
                break
        if user_column == 'stop' or user_row == 'stop':
            break
        board[int(user_row)-1][int(user_column)-1] = chr(9679)
#Switching turns
        turn = True
        for i in board:
            for j in i:
                print(j,"",end="")
            print()
# player 2 codes starts below
#Player 2 code follows the same rules as Player One, it is just adapted to Player Two
    else:
        user_column = input('Player 2 Choose your desired column:' )
        if user_column == 'stop' or user_row == 'stop':
            break
        user_row = input('Player 2 choose your desired row:')
        if user_column == 'stop' or user_row == 'stop':
            break
        while user_column not in in_board or user_row not in in_board:
            print("This space isn't on the board, choose a different place!")
            user_column = input('Player 2 Choose your desired column:' )
            if user_column == 'stop' or user_row == 'stop':
                break
            user_row = input('Player 2 Choose your desired row:')
            if user_column == 'stop' or user_row == 'stop':
                break
        board[int(user_row)-1][int(user_column)-1]
        while board[int(user_row)-1][int(user_column)-1] == chr(9675) or board[int(user_row)-1][int(user_column)-1] == chr(9679):
            print('This Space has already been played, choose a different place!')
            user_column = input('Player 2 Choose your desired column:' )
            if user_column == 'stop' or user_row == 'stop':
                break
            user_row = input('Player 2 Choose your desired row:')
            if user_column == 'stop' or user_row == 'stop':
                break
        if user_column == 'stop' or user_row == 'stop':
            break
        board[int(user_row)-1][int(user_column)-1] =chr(9675)
        turn = False
        for i in board:
            for j in i:
                print(j,"",end="")
            print()
