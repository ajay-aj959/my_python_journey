import time
m = 22

while True:
    for i in range(m):
        for j in range(m):
            if j >= m-i-1  and  j<=i or j>=i and j <= m-i-1:
                print("*",end='')
            else:
                print(" ",end='')
    
        print("\n",end='')
    
        time.sleep(0.01)