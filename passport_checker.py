#take in user input
user_query = input("Enter the name of the file: ")
ORIGINAL_PASS = open(user_query, "r+")

with ORIGINAL_PASS as passer:
    for passer_line in passer:
        element = passer_line.split()
        if element != []:
            print(element)
