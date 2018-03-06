# [ ] Use the `inventory` dictionary in a program that asks the user for a 
#     UPC number, description, unit price, quantity in stock.
# If the item already exists in the inventory, the information is updated, 
#     and your program should display a message that it is updating the entry.
# If the item does NOT exists in the inventory, a new dictionary entry is created, 
#     and your program should display a message that it is creating a new entry.
# Use try/except in the program.


# test cases

# For an existing item
'''
Enter UPC number: 839529
Enter item description: TOMATOS 1LB
Enter unit price: 1.55
Enter item quantity: 21
Existing item, updating: ['TOMATOS 1LB', 1.29, 25]

  UPC   | Description       |  Unit Price  |  Quantity 
-------------------------------------------------------
839529  | TOMATOS 1LB       |         1.55 |      21.00
'''

# For a new item
'''
Enter UPC number: 29430
Enter item description: ORANGE 1LB
Enter unit price: 0.99
Enter item quantity: 40
New item, creating ORANGE 1LB

  UPC   | Description       |  Unit Price  |  Quantity 
-------------------------------------------------------
29430   | ORANGE 1LB        |         0.99 |      40.00
'''

inventory = {847502: ['APPLES 1LB', 1.99, 50], 847283: ['OLIVE OIL', 10.99, 100], 839529: ['TOMATOS 1LB', 1.29, 25], 483946: ['MILK 1/2G', 3.45, 35], 493402: ['FLOUR 5LB', 2.99, 40], 485034: ['BELL PEPPERS 1LB', 1.35, 28], 828391: ['WHITE TUNA', 1.69, 100], 449023: ['CHEESE 1/2LB', 4.99, 15]}


# get UPC from user, handling cases where the input is invalid with try/except
#TODO: Your code goes here

# display message, either "updating" or creating" and then item is being updated display the `value` being updated
#TODO: Your code goes here

# update dictionary entry
#TODO: Your code goes here

# print header including 
# HINT: look at the testing samples shown in comments above for new item and for existing item
#TODO: Your code goes here

# print actual data from the dictionary (See Hint above)
#TODO: Your code goes here


