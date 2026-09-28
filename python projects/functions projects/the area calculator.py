"""
Write a function named calculate_area that takes two parameters: length and width.
Give width a default value of 5.
The function should return (not print!) the calculated area (length * width).
Call the function twice and print the results:
Once passing both arguments (e.g., 10, 10).
Once passing only the length (e.g., 7).

"""

def calculate_area(length, width = 5):
    total = length * width
    return total


result1 = calculate_area(10, 10)
print(f"first test: {result1}")
result2 = calculate_area(7)
print(f"second test: {result2}")





