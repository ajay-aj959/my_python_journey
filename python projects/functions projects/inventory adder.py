"""

Write a function named add_to_stock that takes three parameters: inventory_dict, item_name, and quantity.
Inside the function, use inventory_dict.setdefault(item_name, 0) to ensure the item flag exists.
Increase that item's count inside the dictionary by the given quantity.
(Note: You do not need to return anything! Dictionaries passed into functions modify the original dictionary directly).
"""



def add_to_stock(inventory_dict,item_name,quantity):
    inventory_dict.setdefault(item_name, 0)
    inventory_dict[item_name] +=quantity

stock = {"apple": 10}

add_to_stock(stock, "banana", 5)
add_to_stock(stock, "apple", 5)

print(stock)

