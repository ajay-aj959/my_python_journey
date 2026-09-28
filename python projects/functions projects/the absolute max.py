"""
Goal: Find the largest number in a list manually.

"""

def find_max(number_list):
    highest_so_far = number_list[0]

    for i in number_list:
        if i > highest_so_far:
            highest_so_far = i

    return highest_so_far


my_nums = [4, 18, 9, 27, 3, 14]

highest = find_max(my_nums)

print(highest)

