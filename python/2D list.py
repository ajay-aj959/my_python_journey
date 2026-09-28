#2D LIST

matrix = [

          [20,40],
          [10,30],
          [100,50]
]
print(matrix)

# access values
print(matrix[0])
print(matrix[1])
print(matrix[2])

#access single number

print(matrix[0][0])  # matrix[0][0]  matrix[20,_]
print(matrix[0][1])  # matrix [0][1] matrix[_,40]
print(matrix[1][0])
print(matrix[1][1])
print(matrix[2][0])
print(matrix[2][1])


#Change one value


matrix[0][0] = 400   # matrix[0][0]  matrix[400,_] 
print(matrix)



