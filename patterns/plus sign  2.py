n = 6
e = n/2

for i in range(1, n):
    for j in range(1, n):
        if i==n-e or j == n-e:
            print(" ",end='')
        else:
            print("#",end='')
    print("\n",end='')