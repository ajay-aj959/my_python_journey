"""


Method	                    Description
============================================================================================================================================
update()	            Updates the dictionary with the specified key-value pairs

get()	                Returns the value of the specified key

copy()	                Returns a copy of the dictionary

clear()             	Removes all the elements from the dictionary

items()	                Returns a list containing a tuple for each key value pair

keys()	                Returns a list containing the dictionary's keys

pop()	                Removes the element with the specified key

popitem()	            Removes the last inserted key-value pair

values()	            Returns a list of all the values in the dictionary

setdefault()	        Returns the value of the specified key. If the key does not
                        exist: insert the key, with the specified value

fromkeys()	            Returns a dictionary with the specified keys and value
"""

class8 = {
          "student1": "john",
          "student2": "sam",
          "student3": "alex",
          "student4": "tom"
}
# update()
class8.update({"student5": "jeason"})

print(class8)


# get()
print(class8.get("student1"))

# copy()
newclass = class8.copy()
print(newclass)

#clear()
newclass.clear()
print(f"newclass :{newclass}")

# items()
print(class8.items())

# keys()
print(class8.keys())

# pop()

class8.pop("student1")
print(class8)

# popitem()
class8.popitem()
print(class8)

# values
print(class8.values())


#setdefault()
print(class8.setdefault("student2", "monaco"))

# fromkey()
users = ["bob","sunny","robert"]  #list

user_status = dict.fromkeys(users)   # dict() is dictionary constructor to construct the existing list into dict keys

print(user_status)
