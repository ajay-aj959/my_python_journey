"""
Enter text: Python is easy to learn

Characters: 23
Words: 5
Letter 'a': 1
Contains "Python": True
Uppercase: PYTHON IS EASY TO LEARN

"""


# define string input
txt = input("Enter Text: ")

# characters check
print("characters: ",len(txt))

# words check
print("worlds: ",len(txt.split()))

# count letters
print(f"count letters: {txt.count(input("count: "))}")

# find word
print(f"contains: { input("word: ") in txt}")

# formattng upper case
print(f"upper case: {txt.upper()}")
