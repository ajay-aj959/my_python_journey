i = """hello i am the devil and king and tell me how many times are 28 days in which month """
print("devil " in i)
print("in which " in i)
print("letter" in  i)




print('ajay'not in i)
print("hello" not in i)



# string slice

x = "ajay,magar"
a = ' HELLO WORLD! '

print(x[2:5])  #slice in perticular range start to end slicing start fron end example "hello,world"
               #                                                                       012345678910                               
print(x[:7])   #slice to start
print(x[2:])   #slice to end


# negative slice indexing

print(x[-8:-2])   # slicing start fron end example "hello,world"
                  #                                109876543210


# Modify strings

print(x.upper())                          # upper case using upper()

print(a.lower())                          # lower case using lower()

print(a.strip())                          # The strip() method removes any whitespace from the beginning or the end:

print(a.replace("H","k"))                 # The replace() method replaces a string with another string

print(a.split())                       # The split() method splits the string into substrings if it finds instances of the separator


# string formating

# format method to use string and numbers combine & string  
# {} currly braces use for  placeholders


age = 30
txt = "i am ajay and i am {}"              # use {}  currly braces as place holders
print(txt.format(age))






quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))






