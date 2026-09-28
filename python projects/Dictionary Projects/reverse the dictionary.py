"""
Your Task:
Create an empty dictionary called spanish_to_english = {}.
Write a for loop to go through the original dictionary. 
(Hint: Use .items() to get both words at once!)Inside the loop, 
insert data into your new dictionary so that the Spanish word becomes the key, and the English word becomes the value.
Print spanish_to_english at the end

"""

english_to_spanish = {"one": "uno", "two": "dos", "three": "tres"}
spanish_to_english = {}

for english , spanish in english_to_spanish.items():
    spanish_to_english[spanish] = english

print(spanish_to_english)

