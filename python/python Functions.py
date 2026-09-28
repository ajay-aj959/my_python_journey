
"""

function structure
 def myfun():               # function 'def'define with function name 'myfunc()'
    ...
    ......
myfun()                     # calling function



define function using 'def' keyword




# Arguments

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the 
parentheses. You can add as many arguments as you want, 
just separate them with a comma.






"""


def my_family(fnames):               # "fname" is argument [arguments are often shotened to args in python]
    print(fnames + " Magar")

my_family("Ajay")
my_family("Vijay")
my_family("Anita")
my_family("Atul")
my_family("Viraj")


# Parameters Or Arguments ?

# The terms parameter and argument can be used for the
# same thing: information that are passed into a function.


# Arbitrary Arguments, *args

# If you do not know how many arguments that will be 
# passed into your function, add a * before the parameter 
# name in the function definition

def new_func(*kids):
    print("the youngest child is " + kids[2])
    print(type(kids))

new_func("Ajay", "Viraj", "Atul")


# keyword arguments    [The phrase Keyword Arguments are often shortened to kwargs in Python ]

def my_func(child3, child2, child1):
    print("the youngest child is: " + child3)

my_func(child1= "Viraj", child2= "Ajay", child3= "Atul")



# Arbitrary Keyword Arguments, **kwargs

# If you do not know how many keyword arguments that will
# be passed into your function, add two asterisk: ** before 
# the parameter name in the function definition.

def mycar(**car):
    print("car name was: " + car["model"])


mycar(brand = "Toyota", model = "supra")



# default parameter value

def new_para_func(country = "norway"):
    print("I am from " + country)

new_para_func("India")
new_para_func("England")
new_para_func()
new_para_func("America")




# PASSING A LIST AS AN ARGUMENTS
def fruit_func(food):
    for i in food:
        print(i)


fruits =["apple", "banana", "cherry", "mango"]
fruit_func(fruits)


# Return Values


def return_func(x):
    return 5 * x

print(return_func(3))     # its argument section  x = 3 here     return 15 
print(return_func(5))     # its argument section x = 5 here      return 25



# recursion



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
