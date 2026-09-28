import os
import time


i,j,k = 0, 0, 0
hours = 24
minutes = 60
sec = 60

while True:
    
    for i in range(hours):
        for j in range(minutes):
            for k in range(sec):
                print('_________CLOCK___________')
                print('  Hour:',i,'Min:',j,'Sec:',k)
                print('-------------------------')
                time.sleep(1)
                os.system('cls')