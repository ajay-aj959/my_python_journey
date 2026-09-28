import random

# okk so we have string variable that randomly create password
# 33 - 126
# Anx@#123


x = str()
end_loop = 0
while end_loop != 1:
    x = input("\nwant to generate y/n :")
    if x == 'y':
        for i in range(0,16):
             i = random.randrange(33, 126)
             print(chr(i),end='')
    else:end_loop = 1


