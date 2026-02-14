# PROBLEM 1

# Write a Python program that:
# Takes a sentence as input from the user.
# Removes extra spaces from the beginning and end.
# Converts the sentence to Title Case.
# Counts how many times the letter "a" appears (case-insensitive).
# Finds the first position of the word "is".
# Replaces the word "bad" with "good".
# Prints the final cleaned sentence.


# sentence = input("Enter a text: ")

# sentence = sentence.strip().lower()

# count_a = sentence.count('a')

# pos_is = sentence.find("is")

# sentence = sentence.replace("bad", "good")

# print("Final sentence", sentence.title())
# print("Number of times a appeared: ", count_a)
# print("The index of is =", pos_is)





# PROBLEM 2

# Takes a username as input.
# Removes extra spaces.
# Converts it to lowercase.
# Counts how many times the character "_" appears.
# Finds the position of "@" using both find() and index() (handle error if not found).
# Replaces "admin" with "user".
# Displays the username in UPPERCASE and Title Case.

username = input("Enter your username : ")

username = username.strip().lower()

count_underscore = username.count('_')

pos_find = username.find("@") 

pos_index = username.index("@")

new_username = username.replace("admin", "user")

print("Username in uppercase: ", new_username.upper())
print("Username in titlecase: ", new_username.title())

print("Number of times underscore appears: ", count_underscore)
print("poition of @ using find: ", pos_find)
print("poition of @ using index: ", pos_index)






