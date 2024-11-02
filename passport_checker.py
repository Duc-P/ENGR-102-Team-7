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

def check_cid(passport):
    return None

def check_pid(passport):
    return None

def check_ecl(passport):
    return None

def check_hcl(passport):
    return None

def check_hgt(passport):
    return None

def check_eyr(passport):
    if 'eyr' in passport and (2024 <= int(passport[passport.index('eyr')+2:passport.index('eyr')+6]) <= 2034):
        return True
    return False

'''
def check_iyr(passport_list):
    return None
'''

def check_byr(passport):# take in one passport    
    if 'byr' in passport and (1920 <= int(passport[passport.index('byr')+2:passport.index('byr')+6]) <= 2008):
        return True
    return False

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
