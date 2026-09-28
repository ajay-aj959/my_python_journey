# text formater 

"""
there is messey text string ex. hELLo mY nAme iS aJaY

enter string: hELLo mY nAme iS aJaY 

1. upper case
2. lower case
3. capitlization
4. title
choose formate:



"""


# define string input
txt = str(input("Enter Here: "))

# choose formating
formating = str(input("1.lower case \n2.upper case \n3.capitalization \n4.title\nChoose formating:  "))

# lower case
if formating == "1":
    print(txt.lower())

# upper case
elif formating == "2":
    print(txt.upper())

# capitalization
elif formating == "3":
    print(txt.capitalize())

# title
elif formating == "4":
    print(txt.title())



