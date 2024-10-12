## 12 hour ##
# Make an Empty board for updating
board = []
# make if else statement deciding whether or not 12-hours or military clock is desired
# if twelve hours clock is desired find if the hours are less than twelve
#If hours are more than 12, subtract 12 from hours, and update board with time and PM

if clock_type == '12':
    if int(time_list[0])>12:
        time_list[0] = int(time_list[0] ) - 12
        if time_list[0] >= 10:
            board.append(mat_clock[int(time_list[0])//10])
            board.append(mat_clock[int(time_list[0])%10])
            board.append(mat_clock[":"])
            board.append(mat_clock[int(time_list[1])//10])
            board.append(mat_clock[int(time_list[1])%10])
            board.append(mat_clock['pm'])
        else:
            board.append(mat_clock[int(time_list[0])])
            board.append(mat_clock['colon'])
            board.append(mat_clock[int(time_list[1])//10])
            board.append(mat_clock[int(time_list[1])%10]) 
            board.append(mat_clock['pm'])
#If hours are less than 12, update board to be given time with AM
    else:
        if int(time_list[0]) >= 10:
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
