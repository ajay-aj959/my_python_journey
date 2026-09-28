import random
computer = int()
loop = 0
player = int()

while loop != 1 :

    
    player = int(input("Guess the num: "))
    computer = random.randint(1, 10)
        # player = int(input("Guess the num: "))
    # if player give input more than 10 or 0 
    if player > 10 or player < 1:
        player = int(input("between (1 - 10): "))
    
    if player != computer:
        print(computer)

    else:
        print(computer)
        print("you win!\n ")
        # input after you will for continue play
        loop = input("CONTINUE (y/n): ")
        # consider that loop is str loop = "y" in input but in output its loop = 1
        if loop == "n":
            loop = 1
            # exit loop if not contine
        if loop == "n":
            exit()