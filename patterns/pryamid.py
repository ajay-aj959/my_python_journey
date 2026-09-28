
m = 11


for i in range(m):
    for j in range(m):
        if j >= m-i-1  and  j<=i:
            print("*",end='')
        else:
            print(" ",end='')

    print("\n",end='')
