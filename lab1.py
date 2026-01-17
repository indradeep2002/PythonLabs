# hello world 
print("hello world")
# create a form using input functions and print function 
# 1st user name , 2nd user age, 3rd user address

user_name = input("Enter user name: ")
user_age = int(input("Enter user age: "))
user_address = input("Enter user address: ")

print(user_name)
print(user_age)
print(user_address)

# check a number whether it is even or odd.

if (user_age % 2 == 0):
    print("Your age is Even.")
else:
    print("Your age is Odd.")