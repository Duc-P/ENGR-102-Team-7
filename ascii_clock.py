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
# Date: 9-10-2024

#Allowed chars for replacement in ascii art
allowed_chars = "abcdeghkmnopqrsuvwxyz@$&*="

#Ask user for time, clock type, and char to replace in ascii art
time = input("Enter the time: ")
clock_type = input("Choose the clock type (12 or 24): ")
fav_char = input("Enter your preferred character: ")

if time[0] == "0":
    time = "12:" + time[2] + time[3]

#If the user doesn't put anythin in for char, bypass while loop
if fav_char == "":
    allowed_chars = ""
    
skip = 0
#While the user enters chars that aren't allowed, ask again
while fav_char not in allowed_chars:
    fav_char = input("Character not permitted! Try again: ")
print("")
    
#Use a dictionary to replace chars later on 
replace = {"0": fav_char, "1": fav_char, "2":fav_char, "3": fav_char, "4": fav_char,"5": fav_char,"6": fav_char,"7": fav_char,"8": fav_char,"9": fav_char}

#Split the time into individual characters - keep a copy with a colon and the other with just the digits.
time_split = []
time_split_copy = []
for char in time:
    time_split.append(char)
time_split_copy += time_split
time_split.remove(":")
for i in range(len(time_split)):
    time_split[i] = int(time_split[i])

#Define ascii art by line for am, pm, and digits 0 - 9
line1_am = " A  M   M"
line2_am = "A A MM MM"
line3_am = "AAA M M M"
line4_am = "A A M   M"
line5_am = "A A M   M"

line1_pm = "PPP M   M"
line2_pm = "P P MM MM"
line3_pm = "PPP M M M"
line4_pm = "P   M   M"
line5_pm = "P   M   M"

line1_colon = "  "
line2_colon = ": "
line3_colon = "  "
line4_colon = ": "
line5_colon = "  "

line1_0 = "000 "
line2_0 = "0 0 "
line3_0 = "0 0 "
line4_0 = "0 0 "
line5_0 = "000 "

line1_1 = " 1  "
line2_1 = "11  "
line3_1 = " 1  "
line4_1 = " 1  "
line5_1 = "111 "

line1_2 = "222 "
line2_2 = "  2 "
line3_2 = "222 "
line4_2 = "2   "
line5_2 = "222 "

line1_3 = "333 "
line2_3 = "  3 "
line3_3 = "333 "
line4_3 = "  3 "
line5_3 = "333 "

line1_4 = "4 4 "
line2_4 = "4 4 "
line3_4 = "444 "
line4_4 = "  4 "
line5_4 = "  4 "

line1_5 = "555 "
line2_5 = "5   "
line3_5 = "555 "
line4_5 = "  5 "
line5_5 = "555 "

line1_6 = "666 "
line2_6 = "6   "
line3_6 = "666 "
line4_6 = "6 6 "
line5_6 = "666 "

line1_7 = "777 "
line2_7 = "  7 "
line3_7 = "  7 "
line4_7 = "  7 "
line5_7 = "  7 "

line1_8 = "888 "
line2_8 = "8 8 "
line3_8 = "888 "
line4_8 = "8 8 "
line5_8 = "888 "

line1_9 = "999 "
line2_9 = "9 9 "
line3_9 = "999 "
line4_9 = "  9 "
line5_9 = "999 "

#Put the ascii line variables into lists for easier data retrieval
am = [line1_am, line2_am, line3_am, line4_am, line5_am]
pm = [line1_pm, line2_pm, line3_pm, line4_pm, line5_pm]
zero_ascii = [line1_0, line2_0, line3_0, line4_0, line5_0]
one_ascii = [line1_1, line2_1, line3_1, line4_1, line5_1]
two_ascii = [line1_2, line2_2, line3_2, line4_2, line5_2]
three_ascii = [line1_3, line2_3, line3_3, line4_3, line5_3]
four_ascii = [line1_4, line2_4, line3_4, line4_4, line5_4]
five_ascii = [line1_5, line2_5, line3_5, line4_5, line5_5]
six_ascii = [line1_6, line2_6, line3_6, line4_6, line5_6]
seven_ascii = [line1_7, line2_7, line3_7, line4_7, line5_7]
eight_ascii = [line1_8, line2_8, line3_8, line4_8, line5_8]
nine_ascii = [line1_9, line2_9, line3_9, line4_9, line5_9]

#Put the lists into another list, so that they can be retrieved even easier
clock_ascii = [zero_ascii, one_ascii, two_ascii, three_ascii, four_ascii, five_ascii, six_ascii, seven_ascii, eight_ascii, nine_ascii, am, pm]


ispm = False
#If the user put in a 12 hour clock, but time inputed is 13:00 or later, subtract the first digit by 1, subtract two from the second digit to get time in pm
if clock_type == "12" and len(time_split) == 4 and time_split[1] > 2:
    time_split[1] = time_split[1] - 2
    time_split[0] = time_split[0] - 1
    if time_split[0] == 0:
        time_split.remove(time_split[0])
    ispm = True
    


first_digit = clock_ascii[(time_split[0])]
second_digit = clock_ascii[(time_split[1])]
third_digit = clock_ascii[(time_split[2])]
if len(time_split) == 4:
    fourth_digit = clock_ascii[(time_split[3])]

#Add if statement so that if the user didn't enter a preferred character, no characters are replaced
if fav_char != "":
    #Replace chars in first digit of time
    for i in range(5):
        new_replace = ""
        for char in first_digit[i]:
            if char in replace:
                new_replace += replace.get(char)
            else:
                new_replace += " "
        first_digit[i] = new_replace
    #Replace chars in second digit of time
    for i in range(5):
        new_replace = ""
        for char in second_digit[i]:
            if char in replace:
                new_replace += replace.get(char)
            else:
                new_replace += " "
        second_digit[i] = new_replace
    #Replace chars in third digit of time
    for i in range(5):
        new_replace = ""
        for char in third_digit[i]:
            if char in replace:
                new_replace += replace.get(char)
            else:
                new_replace += " "
        third_digit[i] = new_replace
    #If there are 4 digits of time, replace chars in fourth digit of time
    if len(time_split) == 4:
        for i in range(5):
            new_replace = ""
            for char in fourth_digit[i]:
                if char in replace:
                    new_replace += replace.get(char)
                else:
                    new_replace += " "
            fourth_digit[i] = new_replace


#If 4 digit time and 24 hr clock, output result
if len(time_split) == 4 and clock_type == "24":
    print(first_digit[0] + second_digit[0] + line1_colon + third_digit[0] + fourth_digit[0][:-1])
    print(first_digit[1] + second_digit[1] + line2_colon + third_digit[1] + fourth_digit[1][:-1])
    print(first_digit[2] + second_digit[2] + line3_colon + third_digit[2] + fourth_digit[2][:-1])
    print(first_digit[3] + second_digit[3] + line4_colon + third_digit[3] + fourth_digit[3][:-1])
    print(first_digit[4] + second_digit[4] + line5_colon + third_digit[4] + fourth_digit[4][:-1])
#If 3 digit time and 24 hr clock, output result but only with 3 digits
elif len(time_split) == 3 and clock_type == "24":
    print(first_digit[0] + line1_colon + second_digit[0] + third_digit[0][:-1])
    print(first_digit[1] + line2_colon + second_digit[1] + third_digit[1][:-1])
    print(first_digit[2] + line3_colon + second_digit[2] + third_digit[2][:-1])
    print(first_digit[3] + line4_colon + second_digit[3] + third_digit[3][:-1])
    print(first_digit[4] + line5_colon + second_digit[4] + third_digit[4][:-1])
#If 3 digit time, 12 hr clock, and is PM output result but only with 3 digits
elif len(time_split) == 3 and ispm == True and clock_type == "12":
    print(first_digit[0] + line1_colon + second_digit[0] + third_digit[0] + pm[0])
    print(first_digit[1] + line2_colon + second_digit[1] + third_digit[1] + pm[1])
    print(first_digit[2] + line3_colon + second_digit[2] + third_digit[2] + pm[2])
    print(first_digit[3] + line4_colon + second_digit[3] + third_digit[3] + pm[3])
    print(first_digit[4] + line5_colon + second_digit[4] + third_digit[4] + pm[4])
#If 4 digit time, 12 hr clock, and is PM output result
elif len(time_split) == 4 and ispm == True and clock_type == "12":
    print(first_digit[0] + second_digit[0] + line1_colon + third_digit[0] + fourth_digit[0] + pm[0])
    print(first_digit[1] + second_digit[1] + line2_colon + third_digit[1] + fourth_digit[1] + pm[1])
    print(first_digit[2] + second_digit[2] + line3_colon + third_digit[2] + fourth_digit[2] + pm[2])
    print(first_digit[3] + second_digit[3] + line4_colon + third_digit[3] + fourth_digit[3] + pm[3])
    print(first_digit[4] + second_digit[4] + line5_colon + third_digit[4] + fourth_digit[4] + pm[4])
#If 4 digit time, 12 hr clock, and is AM output result
elif len(time_split) == 4 and ispm == False and clock_type == "12":
    print(first_digit[0] + second_digit[0] + line1_colon + third_digit[0] + fourth_digit[0] + am[0])
    print(first_digit[1] + second_digit[1] + line2_colon + third_digit[1] + fourth_digit[1] + am[1])
    print(first_digit[2] + second_digit[2] + line3_colon + third_digit[2] + fourth_digit[2] + am[2])
    print(first_digit[3] + second_digit[3] + line4_colon + third_digit[3] + fourth_digit[3] + am[3])
    print(first_digit[4] + second_digit[4] + line5_colon + third_digit[4] + fourth_digit[4] + am[4]) 
#If 3 digit time, 12 hr clock, and is AM output result
elif len(time_split) == 3 and ispm == False and clock_type == "12":
    print(first_digit[0] + line1_colon + second_digit[0] + third_digit[0] + am[0])
    print(first_digit[1] + line2_colon + second_digit[1] + third_digit[1] + am[1])
    print(first_digit[2] + line3_colon + second_digit[2] + third_digit[2] + am[2])
    print(first_digit[3] + line4_colon + second_digit[3] + third_digit[3] + am[3])
    print(first_digit[4] + line5_colon + second_digit[4] + third_digit[4] + am[4])
