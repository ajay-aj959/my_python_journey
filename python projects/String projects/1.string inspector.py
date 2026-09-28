# what is a string inspector

"""
string inspector means it tells you about strings details

1.what is string 
2.lengh of string
3. first and last character of string 
4.string is upper or lower case 
5.white speces in string  


"""

import os
# define string input()
character_string = str(input("enter here: "))

os.system("cls")
# print string 
print("String Is : "+ character_string)

# use len function for string length
print("String Length Is: ", len(character_string))

# use string as list so print like string 0 and string len(string)
print("first character: ",character_string[0],"last character: ",character_string[len(character_string)-1])

# use string is upper of lower with if else and upper(),lower() functions
if character_string == character_string.upper():
    print("is String Upper Case: true")
else:
    print("is String Upper Case: false")

# use for loop to inspect white speces in string
space = 0 
for i in range(len(character_string)):
    if character_string[i] == " ":
        space +=1
print("white spaces in string: ",space)



