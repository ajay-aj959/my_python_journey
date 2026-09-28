
# variable casting 

x = str('ajay')
y = int(70)
z = float(6.1)

print('name:',x)
print('weight:',y)
print('height:',z)

#for getting variable type to get the variable type use  type() function in print function 

print(type(x))
print(type(y))
print(type(z))


# legal variable names are 

myvar ='ajay'
my_var = 'ajay'
_my_var = 'ajay'
myVar = 'ajay'
MYVAR = 'ajay'
myvar2 = 'ajay'

print(myvar,my_var,_my_var, myVar,MYVAR,myvar2)


# illegal variable  names

"""
2myvar = 'ajay'
my-var = 'ajay'
my var = 'ajay'

"""

# assign multiple variable at one line
x,y,z = 29, 20, 10

print(x,y,z)


# assign single value to multiple variables
 
x = y = z = 20

print(x,y,z)


# unpacking values 

fruits = ["mango ", "banana", "apple"]
x,y,z = fruits

print(x)
print(y)
print(z)



# packing values

names = []

x,y,z = 'ajay','vijay','atul'

names = x,y,z

print(names)


# use of global keyword

def newfunc():
    global name
    name = "ajay"
newfunc()

print(name)



# DATA TYPES

"""

TEXT TYPE :                str

NUMERIC TYPES:             int, float , complex

SEQUENCE TYPE:             list, tuple, range

MAPPING TYPE:              dict

SET TYPE:                  set, frozenset

BOOLEAN TYPE:              bool

BINARY TYPE:               bytes, bytearray, memoryview


"""


"""
x = "hello world "                                   str
x = 20                                               int
x = 20.5                                             float
x = 1j                                               complex
x = ["ajay","magar"]                                 list
x = ("ajay","magar")                                 tuple
x = range(6)                                         range
x = {"name" : "ajay", "age" : 28}                    dict
x = {"apple","banana","cherry"}                      set
x = frozenset({"apple", "banana", "mango"})          frozenset
x = True                                             bool
x = b"hello"                                         bytes
x = bytearray(5)                                     bytearray
x = memoryview(bytes(5))                             memoryview


"""



# convert numbers and data types

x = 1              # int
y = 2.8            # float
z = 2j             # complex


# convert int to float 
a =float(x)
# convert float to int
b =int(y)
# convert int to complex
c = complex(x)

# use type() function to see data type

print(type(a))
print(type(b))
print(type(c))


# multiline string 

v = """ this massage is for ajay from future here you become multibillioneir
 and you become most important person on this whole planet """


print(v)


# strings are array in python 


print(v[6])


# looping throuth the string

for h in "banana":
    print(h)

# check length of string 
print(len(v)) 

# check string || to check if certain phrase or character is present in a string use keyword "in"

print("on" in v)

print("hello" not in v)



# string slicing

 




