"""
Write a function named check_passing that takes one parameter: grades_dict.
Inside the function, create an empty list called passing_students = [].
Loop through grades_dict using a for loop (hint: use .items()).
If a student's score is 70 or higher, append their name to the passing_students list.
Return the list at the very end of the function.

"""


def check_passing(grades_dict):
    passing_students = []

    for name, score in grades_dict.items():
        if score >= 70:
            passing_students.append(name)
    return passing_students
    
class_grades = {"Alex": 85, "Sam": 60, "Emma": 95}


result = check_passing(class_grades)
print(result)

