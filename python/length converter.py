import os 
i = int()
while i != 1:
    print("\nLENGTH CONVERTER\n")

    inch, feet, meter, km = float(),float(),float(),float()

    print("1.inch\n2.feet\n3.meter\n4.km")
    
    choice = int(input("choose: "))
    
    # value = float(input("enter : "))
        
    
    
    
    # logic behind conversion 
    if choice == 1:
        value = float(input("enter: "))
        inch = value
        feet = value / 12
        meter = value / 39.37
        km = value * 2.54E-5
        
    elif choice == 2:
        value = float(input("enter: "))
        inch = value * 12
        feet = value 
        meter = value / 3
        km = value / 3281
    
    elif choice == 3:
        value = float(input("enter: "))
        inch = value * 39.37
        feet = value * 3.28
        meter = value 
        km = value / 1000
    
    elif choice == 4:
        value = float(input("enter: "))
        inch = value / 2.54E-5
        feet = value * 3280.84
        meter = value * 1000
        km = value 
        
    elif choice > 4 or  choice < 1:
        exit()
    # printing of output and clearing printed input 
    
    os.system('cls')
    print("\nLENGTH CONVERTER\n")
    
    print("1.INCH: ",inch)
    print("2.FEET: ",feet)
    print("3.METER: ",meter)
    print("4.KM: ",km)
    