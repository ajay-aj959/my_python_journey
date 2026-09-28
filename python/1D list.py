
#1D list
numbers = [20,30,100,200]

# print list
print(numbers)


# access list elements individual
print(numbers[0])
print(numbers[3])
print(numbers[1])



# change list element value
numbers[0]=10
print(numbers)

#check length of list
print(len(numbers))

#loop through list
for i in range(len(numbers)):
    print(numbers[i])

#Add a new value (append)
numbers.append(400)
print(numbers)

#8. Remove the last value

numbers.pop()
print(numbers)


#9. Insert anywhere
numbers.insert(3,22)
print(numbers)

#10. Delete an element

del numbers[3]
print(numbers)




