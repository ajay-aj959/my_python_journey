# Access List Items
newlist = ["banana","apple","cherry","mango","orange","kiwi","melon"]
print(newlist)


print(len(newlist))                          # check length of list

newlist2 = ["abc",32,True,20,"name"]         # list can hold different type of data
print(newlist2)

print(type(newlist2))                        # use type() function to check data type

newlist2 = list(("apple","mango","cherry"))   # list constructor to make list

print(newlist[1])                           # access list item by referring index number

print(newlist[-1])                          # negative indexing always refers last item 

print(newlist[2:5])                         # range of indexing  use for specifice range of indexing
print(newlist[:4])                          # prints specific range and start from begining annd end on 4
print(newlist[2:])                          # prints cherry to end 

print(newlist[-4:-1])                       # prints from secound last to mango not include melon


print("mango" in newlist)                   # check if item exist using in keyword return True


# Change List Items
newlist[1] = "brockly"                       # change item values by index number replace
print(newlist)

newlist[1:3] = "spinach",'cucumber'           # change range of items values  replace
print(newlist)


newlist3 = ["apple","banana","cherry","mango"]
newlist3[1:3] = ["watermelon"]                         # replace index 1 and 2 values with watermelon
print(newlist3)




# Add List Items
"""
append()
insert()
extend()

"""

newlist3 = ["apple","banana","cherry","mango"]
newlist0 =["kiwi","watermelon"]

newlist3.append("orange")                        # use append method to add items in a list
print(newlist3)

newlist3.insert(2, "melon")                             # insert a new value in the list using insert() method
print(newlist3)                                        # syntex: listname.insert(index no,"value")

newlist3.extend(newlist0)                              # this is extend() method to add items of other list
print(newlist3)

newtuple=("muskmelon","guva")

newlist3.extend(newtuple)                               # you can also add tuple items into list
print(newlist3)


# Remove List Items
"""
remove()         it removes item by referring value
del              it deletes entire list from program
clear()          it clears whole list to void
pop()            it removes list's item by referring index number if there is index number it will remove last item default


"""
newlist4 =["apple","banana","cherry","mango","orange","kiwi","melon"]

newlist4.remove("apple")
print(newlist4)                                # it removes item by referring value


newlist4.pop(3)                                 # it removes list's item by referring index number if there is index number 
print(newlist4)


newlist4.clear()
print(newlist4)                                 # it clears whole list to void


del newlist4                                    # it will delete entire list from program so you can't print or see list  



# Loop List
loop_list = ["apple","banana","cherry"]

for i in loop_list:                           # i will get every item value by loop
    print(i)

for j in range(len(loop_list)):                # print list bu referring their index number
    print(loop_list[j])


n = 0
while n < len(loop_list):                      # print all items using while loop by their index number
    print(loop_list[n]) 
    n +=1


# List comrehension /shortest syntex for loop
fruits = ["apple","banana","cherry","kiwi","mango"]

character = [x for x in fruits if "a" in x]                      # syntex: newlist = [expression for item in iterable if condition == True]
print(character)

character = [x.upper() for x in fruits]                          # set the values in the list to upper case
print(character)


character =["hello" for x in fruits]                             # set all values in charater list to "hello"
print(character)

character=[x if x != "banana" else "orange" for x in fruits]     # "Return the item if it is not banana, if it is banana return orange".
print(character)


# Sort List
"""
Number Sorting
Alphabetic Sorting
Reverse Sorting
Case insensetive Sorting

"""
numbers = [1, 3, 6, 2, 10]
numbers.sort()
print(numbers)                                                     # sort by Number 


alpha = ["ramesh", "ajay","vijay","mohan","sai","babu"]           
alpha.sort()
print(alpha)                                                         # sort by Alphabets


numbers.sort(reverse=True)                                            # sort Numbers in  reverse  
print(numbers)            


insense = ["Ramesh","ajay","Bablu","chandu","krish"]
insense.sort(key=str.lower)                                            # sort insensitive  
print(insense)



# Copy List

"""
copy()
list()

"""

clist = [1,4,6,3]
newclist = clist.copy()                                              # Copy List Using copy() Method
print(newclist)

char_list = ["name","age","height","weight"]
new_char = list(char_list)                                            # Copy List Using list() Method
print(new_char)

# Join List
"""
'+' sign
extent()

"""
num_list = [1,5,3,7]
alp_list =["name","age","height","weight"]
num_list.extend(alp_list)                                            # Use extend() Method To Join 2 List
print(num_list)


newnum_list =[1,0,6,2]
print(alp_list+newnum_list)                                           # use '+' sign to join 2 list




# List Methods
"""
1. append() 
2. clear()  
3. copy()   
4. count()  
5. extend()
6. index()
7. insert()
8. pop()
9. remove()
10.reverse()
11.sort()

"""

shopping = ["milk","bread","eggs","banana"]
position = shopping.index("bread")                                     # finding index number of by value using index() method
print(position)


shopping.insert(len(shopping), "butter")                                # add value at specific index using insert() method
print(shopping)








"""
Python Collections (Arrays)

There are four collection data types in the Python programming language:

List - List is a collection which is ordered and changeable. Allows duplicate members.
Tuple - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set - Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary - Dictionary is a collection which is ordered* and changeable. No duplicate members.

"""