class BankAccount:

    # constructor 

    def __init__(self, name, acc_number, balance):
        self.name = name
        self.acc_number = acc_number
        self.balance = balance 

    def deposit(self, amount):
        self.balance = self.balance + amount 
        print("Deposited: ", amount)
        return ""

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Withdraw: ", amount)
        return ""

    def check_balance(self):
        print("Availabe Balance: ", self.balance)
        return ""

    
    

    

acc1 = BankAccount("Arindam", 12345, 1000)
acc2 = BankAccount("Ritam", 78912, 2000)
acc3 = BankAccount("Suraj", 23456, 0)

print(acc1.name) # Arindam
print(acc1.acc_number) # 12345
print(acc1.balance) # 1000
print(acc1.deposit(1000))
print(acc1.withdraw(500))
print(acc1.check_balance())
print()

print(acc2.name)
print(acc2.acc_number)
print(acc2.balance)
print(acc2.deposit(3000))
print(acc2.withdraw(3000))
print(acc2.check_balance())
print()

print(acc3.name)
print(acc3.acc_number)
print(acc3.balance)
print(acc3.deposit(4000))
print(acc3.withdraw(500))
print(acc3.check_balance())
print()