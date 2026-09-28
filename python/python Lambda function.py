"""
lambda is a small anonymous function 


A lambda function can take any number of arguments, but can only have one expression.

it return automatically 



SYNTAX :   lambda arguments : expression
"""

# how to write function 
x = lambda a: a+5
print(x(5))

# lambda can take any number of arguments
new_x = lambda a,b : a * b

print(new_x(5, 8))

# multiple argument and expressions 
n = lambda a,b,c : a+b+c

print(n(10, 20, 5))





# use of lambda with real funtions

def myfunc(n):
    return lambda a : a* n

dob = myfunc(2)

print(dob(12))




