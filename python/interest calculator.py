# total amount = principal * rate * time / 100 

principal_amount = float(input("loan amount:Rs. "))
rate = float(input("rate of interest(%): "))
time = float(input("time period(Yr): "))
print("___________________________________________\n")
print("principal amount Rs: ",principal_amount)
print("total interest Rs:", principal_amount * rate * time /100)
print("total amount Rs:", principal_amount * rate * time /100 + principal_amount)
print("\n")