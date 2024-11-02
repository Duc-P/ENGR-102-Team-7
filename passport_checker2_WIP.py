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
# Assignment: Lab 11.10: Passport Checker Part B
# Date: 2-11-2024

def check_cid(passport):
    return None

def check_pid(passport):
    return None

def check_ecl(passport):
    return None

def check_hcl(passport):
    return None

def check_hgt(passport):
    if 'hgt' in passport:
        if 'cm' in passport and (150 <= int(passport[passport.index('cm')-3:passport.index('cm')]) <= 193):
            return True # parsing the 3 digits before the "cm" in hgt and converting it to an int for comparison
        elif 'in' in passport and (59 <= int(passport[passport.index('in')-2:passport.index('in')]) <= 76):
            return True # parsing the 2 digits before the "in" in hgt and converting it to an int for comparison
    return False

def check_eyr(passport):
    if 'eyr' in passport and (2024 <= int(passport[passport.index('eyr')+4:passport.index('eyr')+8]) <= 2034):
        return True # parsing the 4 digits after the ":" in eyr and converting it to an int for comparison
    return False

'''
def check_iyr(passport_list):
    return None
'''

def check_byr(passport):# take in one passport 
    if 'byr' in passport and (1920 <= int(passport[(passport.index('byr')+4):(passport.index('byr')+8)]) <= 2008):
        return True # parsing the 4 digits after the ":" in byr and converting it to an int for comparison
    return False

#take in user input
user_query = input("Enter the name of the file: ")
ORIGINAL_PASS = open(user_query, "r+")
pass_string = ORIGINAL_PASS.read()
ORIGINAL_PASS.close()
pass_list = pass_string.split('\n\n')
valid_passports = 0

for i in pass_list:
    if check_byr(i):
        if check_eyr(i):
            if check_hgt(i):
                if 'hcl' in i:
                    if 'ecl' in i:
                        if 'pid' in i:
                            if 'cid' in i:
                                valid_passports += 1
                                with open('valid_passports.txt', 'a+') as new_file:
                                    new_file.write(i + '\n\n')
print('There are', valid_passports, 'valid passports')
