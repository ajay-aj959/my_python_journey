# what is text cleaner

"""
text clearner is clean the string and remove all unwanted white spaces and unwanted characters/symbols


input string
      ||
strip white spaces
      ||
replace()  unwanted symbold with ""
      ||
split() split every character into list
      ||
join() joint every list element



"""

# define string input
character_string = str(input("Enter Here: "))

# list of unwanter characters
unwanted_characters = "!@#$%^&*()_-+={}[]/><"


# remove white spaces from string
character_string = character_string.strip()

# replace unwanted characters/symbols 
for i in unwanted_characters:
    character_string = character_string.replace(i,"")


# split() string into list elements and join()
character =" ".join(character_string.split())



# print final result
print(character)








