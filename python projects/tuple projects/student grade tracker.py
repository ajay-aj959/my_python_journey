"""

Student Grade TrackerUse tuples inside a list to manage data records that shouldn't change.

-Goal: Manage student records using (student_name, grade) tuples.

-Practice: Iterating through tuples and tuple unpacking.

-Task: Create a list of tuples like [("Alice", 90), ("Bob", 85)]. 
Loop through the list, unpack the name and grade, and calculate the class average.




add student + grade


"""


student_name,grade = input("Student Name: "),int(input("Grade: "))
students = [("ram", 67), ("rahul", 50), ("anuj", 67), ("veer", 88)]

students.append((student_name,grade))
print(students)
