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
# Assignment: Lab 11.9: Passport Checker
# Date: 30-10-2024

def check_cid(passport_list):
    return None

def check_pid(passport_list):
    return None

def check_ecl(passport_list):
    return None

def check_hcl(passport_list):
    return None

def check_hgt(passport_list):
    return None

def check_eyr(passport_list):
    return None

def check_iyr(passport_list):
    return None

def check_byr(passport_list):# take in a single list of all passports
    valid_passport = [] # only valid bday -> pass to next function
    for element in passport_list:
        #print("THIS ELEMENT IS:\n"+element+"\n")
        bool_byr = element[:4] == "byr:"
        if bool_byr: 
            print("THIS ELEMENT IS:\n"+element+"\n")
            temp_byr = int(element[4:8])
            if 1920 <= temp_byr <= 2008:
                #print("hello")
                valid_passport.append(element)
    return None

#take in user input
user_query = input("Enter the name of the file: ")
ORIGINAL_PASS = open(user_query, "r+")
pass_string = ORIGINAL_PASS.read()
ORIGINAL_PASS.close()
pass_list = pass_string.split('\n\n')
valid_passports = 0
for i in pass_list:
    if 'byr' in i:
        if 'eyr' in i:
            if 'hgt' in i:
                if 'hcl' in i:
                    if 'ecl' in i:
                        if 'pid' in i:
                            if 'cid' in i:
                                valid_passports += 1
                                with open('valid_passports.txt', 'a+') as new_file:
                                    new_file.write(i + '\n\n')
print('There are', valid_passports, 'valid passports')
