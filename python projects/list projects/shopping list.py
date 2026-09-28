"""
SIMPLE SHOPPING LIST

start :   shopping =["milk","bread","eggs"]

1. access list items
2. add list items 
3. change list items
4. remove list items

Enter a key to 'a' Add 'r' Remove 'c' Change

SHOPPING LIST
1.milk
2.bread
3.eggs


"""

import os

shopping_list =["","milk","bread","eggs"]
while True:
    
    os.system('cls')
    print("SHOPPING LIST ")
    for i in range(1,len(shopping_list)):
        print(i,shopping_list[i])
    

    choose = input("Enter a key to 'a' Add 'r' Remove 'c' change: ")
   
    if choose == "a":
        shopping_list.append(input("enter: "))

    elif choose == "r":
        shopping_list.remove(input("enter: "))
  
    if choose == "c":
        old_item = input("enter old item: ")
        new_item = input("enter new item: ")
        index = shopping_list.index (old_item)
        shopping_list[index]= new_item

    

    
    for i in range(1,len(shopping_list)):
        print(i,shopping_list[i])
    
    


