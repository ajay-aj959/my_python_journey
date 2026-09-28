

"""
Your Task:
Write a for loop to look at the students. 
(Hint: Use students.items() so you can look at both the name and the score at the same time).
Write an if statement inside the loop to check if a student's score is 70 or higher.
If they scored 70 or higher, print their name.


"""

students = {"Alex": 85, "Emma": 92, "Sam": 68, "Katie": 74, "John": 55}



# first method 

#for i in students.keys():
#    if students[i] >= 70:
#        print(i,":pass")
#
#    else:
#        print(i,":fail")



# secound method

# Python unpacks the key into 'name' and the value into 'score'
for name, score in students.items():
    if score >= 70:
        print(name)

