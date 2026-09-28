"""
sets define and assign with '{}' braces

a set is collection which is unordered and unindexed and no duplicates and unchangable

len function- len(), type function -type(),set consturctor- set()

acess items in set can't acccess item by referring index number to access items use 'in'  keyword

add items use add() method or use update() method to join two sets as one & with update method use can join any itrable(list,tuple,dictionaries)

remove items in set you can remove item using remove() method or discard() method
remove() : if item does not exist it will give you an error
discard(): if item does not exist it will not give you an error 
pop() method to remove last item 
clear() method to clear/empty the set
del keyword to delete set

loop set same as list and tuple

join two sets use 
union() : The union() method returns a new set with all items from both sets:
update() : The update() method inserts the items in set2 into set1:
intersection_update(): keep only the duplicates
intersection(): The intersection() method will return a new set, that only contains the items that are present in both sets.
symmetric_difference_update(): keep all but not duplicates
symmetric_difference():   method will return a new set, that contains only the elements that are NOT present in both sets.




--------------------------------------------------------------------------------------
   Method	                           Description
--------------------------------------------------------------------------------------
   add()	                           Adds an element to the set
   clear()          	               Removes all the elements from the set
   copy()	                        Returns a copy of the set
   update()	                        Update the set with the union of this set and others
   remove()                         Removes the specified element
   pop()	                           Removes an element from the set
   difference()    	               Returns a set containing the difference between two or more sets
   difference_update()	            Removes the items in this set that are also included in another, specified set
   discard()	                     Remove the specified item
   intersection()              	   Returns a set, that is the intersection of two other sets
   intersection_update()	         Removes the items in this set that are not present in other, specified set(s)
   isdisjoint()	                  Returns whether two sets have a intersection or not
   issubset()	                     Returns whether another set contains this set or not
   issuperset()                	   Returns whether this set contains another set or not
   symmetric_difference()	         Returns a set with the symmetric differences of two sets
   symmetric_difference_update()	   inserts the symmetric differences from this set and another
   union()                        	Return a set containing the union of sets
------------------------------------------------------------------------------------------

sets projects

1. Unique Number Cleaner
2. Duplicate Word Finder
3. Common Friends
4. Unique Visitors
5. Permission Checker
6. Set-Based Inventory Checker



"""

#
## sets are unorder print will be random
#myset = {"name","age","height","weight"}
#print(myset)
#
## length of set
#print(len(myset))
#
## data type of itrate
#print(type(myset))
#
## set constructor set()
#myset = set({"age","name","weight","height"})
#
## access item using " in " keyword
#print("age" in myset)
#
#
##add item using add() method 
#myset1 = {"apple","banana","kiwi","orange"}
#
#myset1.add("tomato")
#print(myset1)
#
## use update method to add new to existing one 
#tempset ={"watermelon"}
#
#myset1.update(tempset)
#print(myset1)
#
##to add list elements to sets
#newlist = ["muskmelon","mango"]
#myset1.update(newlist)
#print(myset1)
#
#
##remove set items using remove() method
#myset1.remove("tomato")
#print(myset1)
#
## remove set items using discard() method
#myset1.discard("muskmelon")
#print(myset1)
#
## remove items using pop() method
#myset.pop()
#print(myset)
#
## use clear() method to clear out set
#myset.clear()
#print(myset)
#
## delete set using 'del' keyword
#del myset
#
## loop through set with values
#for i in myset1:
#    print(i)
#
#
## join two sets using union() and update() method
#set1 = {"a","b","c"}
#set2 = {1,2,3}
#set3 = set1.union(set2)
#print(set3)
#
#
## using update() method to insert set2 into set1
#set1.update(set2)
#print(set1)
#
## keep only duplicates using intersect_update()
#x = {"apple","banana","cherry"}
#y = {"google","microsoft","apple"}
#
#x.intersection_update(y)
#print(x)
#
## create new set and return only that present in  both sets
#z = x.intersection(y)
#print(z)
#
#
## keep all but not duplicates
#x = {"apple","banana","cherry"}
#y = {"google","microsoft","apple"}
#x.symmetric_difference_update(y)
#print(x)
#
#
## return set that contains all items from both sets, except item that are present in both
#x = {"apple","banana","cherry"}
#y = {"google","microsoft","apple"}
#
#z = x.symmetric_difference(y)
#print(z)
#
#


# access sets

newset = {"oppo","nokia","iphone","samsung","xiaomi","mi","vivo"}

for i in newset:
   print(i)

print("nokia" in newset)


# add new item

newset.add("realme")
print(newset)

color = {"red"}
newset.update(color)
print(newset)


# remove 

newset.remove("red")
print(newset)


newset.pop()

print(newset)


mobile = set()

mobile = newset.copy()
print(mobile)



fruits = {"mango", "apple", "banana", "orange", "apple"}
myset = {"mango", "apple", "banana", "orange", "apple","kiwi"}



print(myset.intersection(fruits))
print(myset.difference(fruits))






