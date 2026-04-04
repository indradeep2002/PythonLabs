# 📌 Problem Statement

# In real life, we use different payment methods like:

# Credit Card
# Debit Card
# UPI

# Even though the action is the same (making a payment), the process is different for each method.

# Your task is to design a system that demonstrates polymorphism using this scenario.

# 🎯 Requirements

# Create a base class:

# Payment

# with a method:

# pay(amount)
# Create derived classes:
    # CreditCard
    # DebitCard
    # UPI
# Each class should override the pay() method:
    # CreditCard → simulate OTP verification
    # DebitCard → simulate PIN verification
    # UPI → simulate UPI ID confirmation
# Use polymorphism:
    # Store all payment objects in a list
    # Call pay() using a loop


class Payment:
     
     def pay(self, amount):
          print("Payment is processing ....")

class CreditCard(Payment):
     
     def pay(self, amount):
          print(f"Processing Credit card payment {amount} ")
          print("Verifying OTP...")
          print("Payment Successful\n")

class DebitCard(Payment):
     
     def pay(self, amount):
          print(f"Processing Debit card payment {amount} ")
          print("Verifying PIN...")
          print("Payment Successful\n")

class UPI(Payment):
     
     def pay(self, amount):
         print(f"Processing UPI payment {amount} ") 
         print("Verifying UPI ID...")
         print("Payment Successful\n") 

amount = float(input("Enter amount to pay: "))

method = input("Enter payment method: ").lower()

if method == 'credit':
     payment = CreditCard()

elif method == 'debit':
     payment = DebitCard()

elif method == 'upi':
     payment = UPI()

else:
     print("Invalid payment method")
     exit()

payment.pay(amount)
