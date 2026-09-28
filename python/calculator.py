#import os
i = int()
while i != 1:
    num1, operator, num2 = float(input('enter num1:')),input('enter op:' ),float(input('enter num2:'))
    total = float()
    if operator == '+':total = num1+num2
    elif operator == '*':total = num1*num2
    if operator == '/':total = num1/num2
    elif operator == '-':total = num1-num2
    print(total)
#os.system('cls')