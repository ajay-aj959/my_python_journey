# A tuple is a collection which is ordered and unchangeable.

"""
tuples use round backets()
tuple is order,indexed,unchangeable,allow duplicates
length len()
type()

one item in tuple ',' is nessesary else its not tuple ex. mytuple=("ajay",)

to access item same as list using index numbers ex. mytuple[1] and also same for range of tuple items ex. mytuple[2:5] and nagatve indexing ex.mytuple[-1]

check if item exist in tuple list using  'in' keyword

update tuple , tuple is unchangeble so but in order to update/change tuple item conver tuple to list and add item or change items and than convert back to tuple

add item tuple not use 'append()' method so to add item we have to convert in list 

to add two tuple as one we use '+' additon sign  ex.thistuple =+ newtuple or thistuple = thistuple+newtuple

unpacking tuple when we normally assign tuple and add values this is called 'packing' a tuple but python allowed to extract the values back into variables and this 'unpacking'

using astrisk '*'
If the number of variables is less than the number of
values, you can add an * to the variable name and the
values will be assigned to the variable as a list:


If the asterisk is added to another variable name than the 
last, Python will assign values to the variable until the 
number of values left matches the number of variables left.



loops in tuple is as same in list

join tuples use '+' 
or
Multiply Tuples
If you want to multiply the content of a tuple a given 
number of times, you can use the '*' operator





tuple methods
1.count
2.index

"""


#assign tuple
first_tuple = ("apple","banana","kiwi","orange","papaya","berry")
print(first_tuple)
# length of tuple
print(len(first_tuple))

# use of type() function
print(type(first_tuple))

# single item in tuple using ','
single_tuple =("mango",)
print("single tuple:",type(single_tuple))

# access items of tuple same like list
print("access single item:",first_tuple[1])
print("access negative indexing:",first_tuple[-1])
print("access range of items:",first_tuple[2:5])
print("access in range first:",first_tuple[2:])
print("access in last range:",first_tuple[:5])


# check item exist in tuple using 'in' keyword
print("yes item found in tuple" ) if "berry" in first_tuple else print("item not found in tuple")

# update tuple , tuple is unchangeble but we use tuple constructor  to convert tuple in list and change value and convert it back to tuple
second_tuple = ("ajay","ram","ramesh","rahul")

newlist = list(second_tuple)  # convert tuple to list

newlist[1] = "vijay"    # change
newlist.remove("ramesh")  # remove
newlist.append("atul")   # add
second_tuple = tuple(newlist)  # converting list to tuple 
print(second_tuple)

# add two tuple as one we use '+' sign 
phones = ("oppo","vivo","nokia","realme","xaiomi","mi")
phone_list=("samsung","apple")

#phones = phones + phone_list
#phones +=phone_list
print(phones + phone_list)

# unpacking tuples
android , ios = phone_list

print(android)
print(ios)


# use of astrisk*
new_phone,*other = phones
print(other)
print(new_phone)

#using *astrisk we can unpack last item 
*mytuple , last_phone = phones     
print(mytuple)
print(last_phone)



# loop in tuple is same as in list

# loop through values
for i in phones:
    print(i)

# loop through index number
for x in range(len(phone_list)):
    print(phone_list[x])
   


# multiply tuple by given time using '*'
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# tuple methods 

# index method
item  = phones.index("oppo")
print(item)

# count method
print(phones.count("vivo"))


