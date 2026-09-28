import random
player = int()
loop =int()
computer = int()
result = 0


while loop != 1:

    computer = random.randint(1, 3)
    print("1.rock\n2.paper\n3.scissor")
    player = int(input("enter choice: "))
    print("___________________________")

    # ===================WIN===========================

    if player == 1 and computer == 3 :
        print("player: rock")
        print("computer: scissor")
        print("You Win!")

    elif player == 2 and computer == 1:
        print("player: paper")
        print("computer: rock")
        print("You Win!")

    elif player == 3 and computer == 2:
        print("player:scissor")
        print("computer: paper")
        print("You Win!")
    

# =========================LOSE=============================

    if player == 3 and computer == 1:
        print("player: scissor")
        print("computer: rock")
        print("You Lose!")

    elif player == 1 and computer == 2:
        print("player: rock")
        print("computer: paper")
        print("You Lose!")

    elif player == 2 and computer == 3:
        print("player:paper")
        print("computer: scissor")
        print("You Lose!")
    
# ===========================TIE====================================
    if player == 1 and computer == 1:
        print("player: rock")
        print("computer: rock")
        print("Tie !")

    elif player == 2 and computer == 2:
        print("player: paper")
        print("computer: paper")
        print("Tie !")

    elif player == 3 and computer == 3:
        print("player:scissor")
        print("computer: scissor")
        print("Tie !")

    print("___________________________")
