"""
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
user_col = 1 # second input

while user_row != "stop" or user_col != "stop": 
         break

for i in board:
    for j in i:
        print(j,"",end="")
    print()


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
user_col = 1 # second input

while user_row != "stop" or user_col != "stop":
    for i in board:
        for j in i:
            print(j,"",end="")
        print()
    user_row = input("Enter Row: ")
    user_col = input("Enter Column: ")
    board[int(user_row) - 1][int(user_col) - 1] = chr(9675)"""
"""
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
user_col = 1 # second input

while user_row != "stop" or user_col != "stop": 
    if turn == False:
        user_column = int(input('Player 1 Choose your desired column:' ))
        user_row = int(input('Player 1 Choose your desired row:'))
        if user_column == 'stop' or user_row == 'stop':
            break
        board[user_row-1][user_column-1]
        while board[user_row-1][user_column-1] == chr(9675) or board[user_row-1][user_column-1] == chr(9679):
            print('This Space has already been played, choose a different place!')
            user_column = int(input('Player 1 Choose your desired column:' ))
            user_row = int(input('Player 1 Choose your desired row:'))
        board[user_row-1][user_column-1] = chr(9679)
        turn = True
        for i in board:
            for j in i:
                print(j,"",end="")
            print()
    else:
        user_column = int(input('Player 2 Choose your desired column:' ))
        user_row = int(input('Player 2 choose your desired row:'))
        if user_column == 'stop' or user_row == 'stop':
            break
        board[user_row-1][user_column-1]
        while board[user_row-1][user_column-1] == chr(9675) or board[user_row-1][user_column-1] == chr(9679):
            print('This Space has already been played, choose a different place!')
            user_column = int(input('Player 1 Choose your desired column:' ))
            user_row = int(input('Player 1 Choose your desired row:'))
        board[user_row-1][user_column-1] =chr(9675)
        turn = False
        for i in board:
            for j in i:
                print(j,"",end="")
            print()
"""

"""
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
user_col = 1 # second input
stop = ""

while user_row != "stop" or user_col != "stop": 
    if turn == False:
        for i in board:
            for j in i:
                print(j,"",end="")
            print()
        stop = input("Do you want to stop playing? ")
        if stop.lower() == "stop":
            break
        user_column = int(input('Player 1 Choose your desired column:' ))
        user_row = int(input('Player 1 Choose your desired row:'))
        if user_column == 'stop' or user_row == 'stop':
            break
        board[user_row-1][user_column-1]
        while board[user_row-1][user_column-1] == chr(9675) or board[user_row-1][user_column-1] == chr(9679):
            print('This Space has already been played, choose a different place!')
            stop = input("Do you want to stop playing? ")
            if stop.lower() == "stop":
                break
        if stop.lower() == "stop":
            break
            user_column = int(input('Player 1 Choose your desired column:' ))
            user_row = int(input('Player 1 Choose your desired row:'))
        board[user_row-1][user_column-1] = chr(9679)
        turn = True

    else:
        for i in board:
            for j in i:
                print(j,"",end="")
            print()
        stop = input("Do you want to stop playing? ")
        if stop.lower() == "stop":
            break
        user_column = int(input('Player 2 Choose your desired column:' ))
        user_row = int(input('Player 2 choose your desired row:'))
        if user_column == 'stop' or user_row == 'stop':
            break
        board[user_row-1][user_column-1]
        while board[user_row-1][user_column-1] == chr(9675) or board[user_row-1][user_column-1] == chr(9679):
            stop = input("Do you want to stop playing? ")
            if stop.lower() == "stop":
                break
        if stop.lower() == "stop":
            break
            print('This Space has already been played, choose a different place!')
            user_column = int(input('Player 1 Choose your desired column:' ))
            user_row = int(input('Player 1 Choose your desired row:'))
        board[user_row-1][user_column-1] =chr(9675)
        turn = False
"""

 board = [[".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".",".",".",".",".",".","."]]

"""
turn = False # flip flop b/w True and False
user_row = 1 # first input 
user_col = 1 # second input

while user_row != "stop" or user_col != "stop": 
    if turn == False:
        user_column = input('Player 1 Choose your desired column:' )
        user_row = input('Player 1 Choose your desired row:')
        if user_column == 'stop' or user_row == 'stop':
            break
        board[int(user_row)-1][int(user_column)-1]
        while board[int(user_row)-1][int(user_column)-1] == chr(9675) or board[int(user_row)-1][int(user_column)-1] == chr(9679):
            print('This Space has already been played, choose a different place!')
            user_column = input('Player 1 Choose your desired column:' )
            user_row = input('Player 1 Choose your desired row:')
        board[int(user_row)-1][int(user_column)-1] = chr(9679)
        turn = True
        for i in board:
            for j in i:
                print(j,"",end="")
            print()
    else:
        user_column = input('Player 2 Choose your desired column:' )
        user_row = input('Player 2 choose your desired row:')
        if user_column == 'stop' or user_row == 'stop':
            break
        board[int(user_row)-1][int(user_column)-1]
        while board[int(user_row)-1][int(user_column)-1] == chr(9675) or board[int(user_row)-1][int(user_column)-1] == chr(9679):
            print('This Space has already been played, choose a different place!')
            user_column = input('Player 1 Choose your desired column:' )
            user_row = input('Player 1 Choose your desired row:')
        board[int(user_row)-1][int(user_column)-1] =chr(9675)
        turn = False
        for i in board:
            for j in i:
                print(j,"",end="")
            print()
"""
"""
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
user_col = 1 # second input

while user_row != "stop" or user_col != "stop": 
    if turn == False:
        user_column = input('Player 1 Choose your desired column:' )
        if user_column == 'stop' or user_row == 'stop':
            break
        user_row = input('Player 1 Choose your desired row:')
        if user_column == 'stop' or user_row == 'stop':
            break
        board[int(user_row)-1][int(user_column)-1]
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
        turn = True
        for i in board:
            for j in i:
                print(j,"",end="")
            print()
    else:
        user_column = input('Player 2 Choose your desired column:' )
        if user_column == 'stop' or user_row == 'stop':
            break
        user_row = input('Player 2 choose your desired row:')
        if user_column == 'stop' or user_row == 'stop':
            break
        board[int(user_row)-1][int(user_column)-1]
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
        board[int(user_row)-1][int(user_column)-1] =chr(9675)
        turn = False
        for i in board:
            for j in i:
                print(j,"",end="")
            print()
"""

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
user_col = 1 # second input
in_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

while user_row != "stop" or user_col != "stop": 
    if turn == False:
        user_column = input('Player 1 Choose your desired column:' )
        if user_column == 'stop' or user_row == 'stop':
            break
        user_row = input('Player 1 Choose your desired row:')
        if user_column == 'stop' or user_row == 'stop':
            break
        while user_column not in in_board or user_row not in in_board:
            print("This space isn't on the board, choose a different place!")
            user_column = input('Player 1 Choose your desired column:' )
            if user_column == 'stop' or user_row == 'stop':
                break
            user_row = input('Player 1 Choose your desired row:')
            if user_column == 'stop' or user_row == 'stop':
                break
        board[int(user_row)-1][int(user_column)-1]
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
        turn = True
        for i in board:
            for j in i:
                print(j,"",end="")
            print()
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
            user_column = input('Player 1 Choose your desired column:' )
            if user_column == 'stop' or user_row == 'stop':
                break
            user_row = input('Player 1 Choose your desired row:')
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
