"""
Your Task:
Write a for loop to look at each fruit in the words list.
Inside the loop, use word_counts.setdefault(fruit, 0) to tell Python:
 "If this fruit is a new flag, insert it with a starting count of 0. 
 If it's already there, just give me its current count.
 "Increase that fruit's count in the dictionary by 1.
 Print word_counts at the end

"""


words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = {}


for fruits in words:
    word_counts.setdefault(fruits, 0)
    word_counts[fruits]+=1

print(word_counts)