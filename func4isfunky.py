
def make_number(str2, str1):
    puzzle_letters = list(str1)
    user_letters = list(str2)
    user_num = ""
    for x in range(len(user_letters)):
        if user_letters[x] in puzzle_letters:
            user_num += str(puzzle_letters.index(user_letters[x]))
    return int(user_num)

"""
def make_numbers(puzzle_str, user):
    dividend = make_number(str2, str1)
    quotient = make_number(str2, str1)
    divisor = make_number(str2, str1)
    remainder = make_number(str2, str1)
    return tuple(dividend, quotient, divisor, remainder)
"""