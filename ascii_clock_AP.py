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

#character
allowed_chars = "abcdeghkmnopqrsuvwxyz@$&*="
fav_char = input("Enter your preferred character: ")
while fav_char not in allowed_chars:
    fav_char = input("Character not permitted! Try again: ")
