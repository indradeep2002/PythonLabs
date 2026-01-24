#print the following patterns: 

# * -> 1st row
# * *
# * * *
# * * * *
# * * * * *

#for loop , user input

user_input = int(input("Enter user input for row & coloumn: ")) 

for i in range(user_input):#creating rows 0, 1, 2, 3, 4
    for j in range(i+1): # i+1 -> 1 , j->0 star printed 
        print("*", end=" ") # print * and space 
    print() #new line create 




#    *
#   ***
#  *****
# *******
#*********

for i in range(user_input): #row 5 - i if i = 0 5 - i = 5-0 = 5
    for j in range(user_input - i): #i = 0, 5-i = 5 - 0 = 5, 0, 1, 2, ,3,4
        print(" ", end="") # space printing first 
    
    # 2 * i - 1 

    for k in range(2 * i - 1):
        print("*", end="")

    print()
print()



# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(user_input, 0, -1):
    for j in range(i):
        print("*", end=" ") #elements print 
    print() #new line print 


 




