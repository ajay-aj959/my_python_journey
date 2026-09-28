import random
import os
import time
loop = int()
user = str()
dice = 0



while loop !=1:
    
    user = input("Roll Dice (y/n): ")
    os.system('cls')
    if user == "y":
        dice = random.randint(1, 6)
    else:exit()

    time.sleep(0.2)

    if dice == 1:
        print("[=====]")
        print("[     ]")
        print("[  o  ]")
        print("[     ]")
        print("[=====]")
        
    
    if dice == 2:
        print("[=====]")
        print("[     ]")
        print("[ o o ]")
        print("[     ]")
        print("[=====]")
    
    if dice == 3:
        print("[=====]")
        print("[     ]")
        print("[o o o]")
        print("[     ]")
        print("[=====]")
    
    if dice == 4:
        print("[=====]")
        print("[o   o]")
        print("[     ]")
        print("[o   o]")
        print("[=====]")
    
    if dice == 5:
        print("[=====]")
        print("[o   o]")
        print("[  o  ]")
        print("[o   o]")
        print("[=====]")
        
    if dice == 6:
        print("[=====]")
        print("[ o o ]")
        print("[ o o ]")
        print("[ o o ]")
        print("[=====]")
    
    