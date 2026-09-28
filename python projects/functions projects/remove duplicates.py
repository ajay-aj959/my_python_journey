"""

remove duplicates



"""


def remove_duplicates(numbers):
    duplicates  = []
    no_dup =[]
    for i in numbers:
        if i not in no_dup:
            no_dup.append(i)
        else:
            duplicates.append(i)

    return no_dup


raw_data=[1, 2, 2, 3, 4, 4, 5]

result = remove_duplicates(raw_data)
print(result)
        
    