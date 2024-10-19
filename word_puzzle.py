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
# Assignment: lab Topic 9
# Date: 14-10-2024

def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")
'''
def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    puzzle = "RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"
    print()
    print_puzzle(puzzle)

if __name__ == '__main__':
    main()
'''
def get_valid_letters(x):
    #Make a list of all valid letters, then for every individual letter in puzzle stirng, add that to a list and convert that list to a string.
    char_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    puzzle_list = list(x)
    valid_letter_list = []
    for i in puzzle_list[:]:
        if i in char_list:
            if i not in valid_letter_list:
                valid_letter_list.append(i)
    valid_letter_string = ''.join(valid_letter_list)
    return valid_letter_string

def is_valid_guess(x, y):
    #Test if every character in a guess is a valid letter, and that each letter only appears once.
    valid_letter_list2 = list(x)
    
    user_guess_list = list(y)
    valid_letter_list2.sort()
    user_guess_list.sort()
    if user_guess_list == valid_letter_list2:
        return True
    else:
        return False
def check_user_guess(dividend, quotient, divisor, remainder):
    #Check if the guess is correct using formula given.
    right_side = quotient * divisor + remainder
    if dividend == right_side:
        return True
    else:
        return False
    
def make_number(str2, str1):
    #Take guess and individual word and convert to a value
    puzzle_letters = list(str1)
    user_letters = list(str2)
    user_num = ""
    for x in range(len(user_letters)):
        if user_letters[x] in puzzle_letters:
            user_num += str(puzzle_letters.index(user_letters[x]))
    return int(user_num)

def make_numbers(puzzle_string, user_guess):
    # Make a list of each individual'word' in the puzzle
    puzzle_words = []
    puzzle_list3 = list(puzzle_string)
    j = puzzle_list3.count(' ')
    for i in range(j):
        puzzle_list3.remove(' ')
    k = puzzle_list3.index('|')
    puzzle_list3[k]=','
    puzzle_list3 = ('').join(puzzle_list3)
    puzzle_words = puzzle_list3.split(',')
    #Assign dividend, quotient, divisor, and remainder based off format.
    dividend = puzzle_words[2]
    quoteint = puzzle_words[0]
    divisor = puzzle_words[1]
    remiander = puzzle_words[-1]
    x = make_number(dividend, user_guess)
    y = make_number(quoteint, user_guess)
    z = make_number(divisor, user_guess)
    w = make_number(remiander, user_guess)
    
    return_tuplre = (x, y, z, w)
    return return_tuplre
def main():
    #Combine all made functions to test if guess is correct.
    user_input= input('Enter a word arithmetic puzzle: ')
    print()
    print_puzzle(user_input)
    print()
    user_guess = input('Enter your guess, for example ABCDEFGHIJ: ')
    valid_letter_string = get_valid_letters(user_input)
    if is_valid_guess(valid_letter_string, user_guess) == True:
        dividend, quotient, divisor, remainder = make_numbers(user_input, user_guess)
        if check_user_guess(dividend, quotient, divisor, remainder) == True:
            print('Good job!')
        else:
            print('Try again!')
    else: 
        print('Your guess should contain exactly 10 unique letters used in the puzzle.')


if __name__ == '__main__':
    main()
