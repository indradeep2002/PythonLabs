# Lab Problem: ATM Withdrawal System
# Scenario

# You are creating a simple ATM withdrawal program. A user wants to withdraw money from their bank account using a terminal.

# However, many things can go wrong:

# The user might enter text instead of a number.

# The user might enter a negative number.

# The user might try to withdraw more money than available.

# Your program should handle these situations using try and except so the program does not crash.


# Write a Python program that:

# Starts with a bank balance of ₹10,000.

# Asks the user to enter the amount they want to withdraw.

# Uses a try–except block to handle errors.

# The program should handle these cases:

# If the user enters non-numeric input, show
# "Invalid input! Please enter a number."

# If the withdrawal amount is greater than the balance, show
# "Insufficient balance."

# If the withdrawal amount is negative, show
# "Withdrawal amount cannot be negative."

# If everything is valid:

# Deduct the amount

# Print the remaining balance

balance = 10000 


try:
    amount = int(input("Enter amount to withdraw: ")) #-3000

    if amount < 0:
        print("Withdrawal amount cannot be negative.")
    

    elif amount > balance:
        print("Insufficient Balance!")

    else:
        print("Withdrawl Successful!")
        print("Remining Balance: ", balance - amount)

except ValueError:
    print("Invalid input! Please enter a number.")


