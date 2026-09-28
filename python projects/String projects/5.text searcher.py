# text searcher 

"""
you can search any word from string 
if string output true found else not found

"""

# Define String input
character_string = str(input("Enter Here: "))

# Define word search input
word = str(input("Enter word: "))

# build logic
if word in character_string:
    print("found")
else:
    print("not found")

