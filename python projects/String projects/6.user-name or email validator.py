# what is user name and email validator

"""
username/email validater

it checks email formate ex. ajay123@gmail.com

1. check email starts with ajay
2. check email ends with .com
3. check where is @ in email and .
4. check is there numbric value after startswith


"""



# define string input 
email = str(input("Enter Email: "))

# check email starts with ajay+numbric+find @ and endswitch .com
if  email.startswith("ajay") and email.endswith ("gmail.com")and "@" in email:
    print("valid")
else:
    print("invalid")


    

