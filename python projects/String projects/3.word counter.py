# what is world counter 

"""
word counter is count word using len() and split()
first we split() string to string become list and count list elements using len()


"""

# Define String Input
character_string = str(input("Enter Here: "))

# Split() String Into List to Len() elemrnts
txt = len(character_string.split()) 

# final print
print("words: ",txt)