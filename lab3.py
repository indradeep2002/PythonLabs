# TASK1 - SUM OF NATURAL NUMBERS USING WHILE LOOP 

#n = int(input("Enter the number: "))

#sum_of_all = 0

#i = 1

#while (i < n):
#    sum_of_all += i # 0 1 3 6 10
#    i += 1 # 1 2 3 4 5

#print(f"The sum of all values upto {n} is : ", sum_of_all)


# TASK2 - IDENTIFY THE SMALLEST NUMBER UAING WHILE LOOP

#smallest_num = 99999
#count = int(input("How many inputs: "))

#i = 0

#while (i < count):
#    n = int(input("Enter the number: "))
#
#    if smallest_num > n :
#        smallest_num = n

#    i += 1

#print("The smallest num is : ", smallest_num)




# TASK3 - PASSWORD CHECKER USING WHILE LOOP 

#correct_password = 779783
#count = 1

#while True:
#    n = int(input("Enter Your Password: "))

#    if count == 5:
#        print("You have reached maximum number of trails!..")
#        print("Please try again later!")
#        break 

#    if correct_password != n:
#        count += 1
#        print("Try Again!")

#    else:
#        print("Access Granted!")
#        break 


# TASK4 - NUMBER GUESSING GAMING USING BREAK AND WHILE 
#import random 

#secret_number = random.randint(1, 50)



#print("Welcome to The Number Guessing Game!")
#print("Guess a number between 1 and 50!")

#while True:
#    n = int(input("Enter your guess...: ") )

#    if n < secret_number:
#        print("Too low! Try Again..!")

#    elif n > secret_number:
#       print("Too Big! Try Again..! ")

#    else:
#        print("Yay! you have got the answer..")
#        break 



# TASK5 - VIP ENTRY GAME 

#while True :
#    code = int(input("Please Enter Your Code:  "))

#    if code % 5 != 0:
#        print("You are not a VIP!")
#        print("Get Away..")

#    else:
#        print("Granted Access!")
#        break 



# TASK6 - MARIO BROTHER WOODEN FOREST LOST GAME FUNCTION.

print("Welcome to the Wooden Forest Lost Game!")

print()

print("To move up press u")
print("To move down press d")
print("To move left press l")
print("To move right press r")

print()
print()

while True:
    print()
    print("###################")
    print("                  #")
    print("                  #")
    print("         P        #")
    print("                  #")
    print("###################")

    print()

    n = input("I am lost in the wood... enter command: ")

    if n != 'd':
        continue

    else:
        print("Yay i got out of the woods :-)")
        break 



