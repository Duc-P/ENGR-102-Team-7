#take in user input
user_query = input("Enter the name of the file: ")
ORIGINAL_PASS = open(user_query, "r+")
pass_string = ORIGINAL_PASS.read()
ORIGINAL_PASS.close()
pass_list = pass_string.split('\n\n')
print(pass_list)
