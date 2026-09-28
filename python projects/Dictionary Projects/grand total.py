"""
Your Task:
Initialize a variable named total_cost to 0.
Write a for loop that goes through the values of the dictionary.
Add each price to your total_cost variable.
Print the final total at the end.

"""


total_cost = 0
prices = {"milk": 2.50, "bread": 1.99, "eggs": 3.49, "butter": 2.10}


for i in prices.values():
    total_cost = total_cost+i

print(total_cost)

