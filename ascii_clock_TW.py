# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Townsend Wheeler
# Section:      518
# Assignment:   Module 8 team lab (individual component)
# Date:         13-10-2024
#

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
