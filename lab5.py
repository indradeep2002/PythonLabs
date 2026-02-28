
# Lab Problem : Online Shopping Cart Analysis
# You are building a simple system to analyze customer purchases in an online store.
# Each customer buys multiple items.
# Problem Statement
# Take input of purchased items separated by space.
# Store them in a list.
# Convert items into a set to find unique products purchased.
# Store store information in a tuple:
# Store Name
# Location
# GST Number
# Perform the following:
# Print total items purchased.
# Print unique items purchased.
# Print how many times each item was bought.
# Try modifying the tuple and observe what happens.


items_input = input("Enter purchase items separated by space : ").lower() #input

items_list = items_input.split(" ") #list 

unique_items = set(items_list) #converted into set

store_info = ('SuperMart', 'Kalna', 'GST1234')

#calculating total items using loops
total_items = len(items_list)

# for item in items_list:
#     total_items += 1

unique_total_items = 0

for item in unique_items:
    unique_total_items += 1



print("\n----- Shopping Summary ------ ")
print("Total Items Purchased : ", total_items)
print("Total Unique Items Purchased : ", unique_total_items)
print("Item Purchase Count: \n")
for item in unique_items:
    print(item, ":", items_list.count(item))

try:
    store_info[0] = 'SmartBazar'
except TypeError:
    print("\nTuple Modification Error")

print('Store Info: ', store_info)


