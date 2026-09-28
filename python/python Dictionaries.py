# dictionaries are orderd and changeble and not allowed duplicates


# how to assign dict
phone = {
    "Name": "oppo",
    "model": "f17",
    "year": "2026"
}

# print output
print(phone)


# check type()
print(type(phone))

# check length len() length is count based on keys only
print(len(phone))


# how to access dict you can access indivisual part of dict but not by index number but by 'key' 
print(phone["Name"])

# access dict with get() method
print(phone.get("model"))


# get all keys using keys() method
print(phone.keys())


#The list of the keys is a view of the dictionary, 
# meaning that any changes done to the dictionary will be reflected in the keys list.

phone["color"] = "blue"
print(phone)


# how to get list of values in dictionary using values() method
print(phone.values())

# The list of the values is a view of the dictionary,
#  meaning that any changes done to the dictionary will be reflected in the values list.

phone["year"] = 2020
print(phone)

# Get Items using Items() method return items will be  tuples as a list
x = phone.items()
print(x)


# check if key exist in dict using "in" keyword
print("size" in phone )

# change indivisual values by referring key name
phone["color"] = "red"
print(phone)


# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
car = {
       "Name": "LandRover",
       "Model": "defender",
       "price": "2cr",
       "year": "2030"
}
 
car.update({"year": "2029"})
print(car)


#add value to dict to add new value you will need assign new key with value
car["color"] = "blue"
print(car)


# remove items from dictionary using pop() method 
# remove item by key name
car.pop("color")
print(car)

# remove last inserted item using popitem() method
car.popitem()
print(car)

# delete item using delete 'del' keyword  
# delete indivisual item you can also delete dict

del car["Model"]
print(car)

# clear dict using clear()
car.clear()
print(car)


# Looping through dict

# there is four mrthod to looping in dict
# method 1

for i in phone:
    print(i)                              # print all key names
    print(phone[i])                       # print all dict key and values

# method 2 looping  by keys()
for j in phone.keys():    
    print(j)                              # print all key names
    print(phone[j])                       # printing all dict key and values

# method 3 looping by values()
for n in phone.values():
    print(n)                              #print all values only
    

# method 4 looping by items() this loop called iterable unpacking loop
for a,b in phone.items():
    print(a,b)                           #print all keys and values 



# Copy Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, 
# because: dict2 will only be a reference to dict1, and changes 
# made in dict1 will automatically also be made in dict2.

# to copy dict we use copy() Method 

#  copy() method
phone2 = phone.copy()
print(phone2)

# another method is dict()
# dict()
phone3 = dict(phone)
print(phone3)

# Nested dictionaries

school = {
          "student1": {
            "name": "raju",
            "grade": "B"
          },

          "student2": {
            "name": "sam",
            "grade": "A",
          },

          "student3": {
            "name": "john",
            "grade": "A+"
          }
}

print(school)

person1 = {
        "name": "sam",
        "age":  "22"
}

person2 = {
           "name": "john",
           "age":  "21"
}

person3 = {
           "name": "raju",
           "age":  "24"
}


data = {
        "person1": person1,
        "person2": person2,
        "person3": person3
}

print(data)




                 