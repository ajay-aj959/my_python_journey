import os
import random
import time
import msvcrt

snake = [
    [5,8],
    [5,9]
    
]
control = False             # use for control snake[1] not take head position untile key-press
flick = False             # control tail increse loop for flickring tail 1
keydown = 0
gameover = False
direction = 'void'
speed = 1
width ,height = 20,15
xfood ,yfood = 10,6
xtemp, ytemp = 0,0
xprev , yprev = snake[0]
key = 0
tail = 0
score = 0
highscore_path = "D:/Programming/PYTHON/snake_highscore.txt"
highscore= 0


os.system("cls")

while True:

    time.sleep(0.2)  


            
     # gameover logic in if statment
     


    if gameover ==True:
 

        speed = 0  
        control = False 
        os.system('cls')
    

        # reading highscore from file
        with open(highscore_path, "r") as file:
            highscore = file.read()

        # writing highscore in file
        if int(highscore) < score:
            with open(highscore_path, "w") as file:
                file.write(str(score))

        # reading highscore from file and printing
        print("\tGAME-OVER!\n\n")
        with open(highscore_path, "r") as file:
            highscore = file.read()
            print(f"SCORE: {score} \t HIGHSCORE: {highscore}\n")


        print('\n')
        time.sleep(5)
        msvcrt.getch()

    
    
    

   

    if control == True:
        xprev,yprev= snake[0]               # store snake's old coordinates into prev variables
        

    # running getch() inside kbhit() not input logic
    if msvcrt.kbhit():
        control = True
        flick = True
        key = msvcrt.getch()

    # snake direction logic not to reverse direction 
    
    if key == b'w'  and direction != 'down':direction = 'up' 
    elif key == b's' and direction != 'up' :direction = 'down'
    elif key == b'a' and direction != 'right' :direction = 'left'
    elif key == b'd' and direction != 'left' :direction = 'right'
    if gameover == True:
        if key !=b'w'or b's' or b'a' or b'd':
            break
       
              

    if direction == 'up':snake[0][1] -=1
    elif direction == 'down' :snake[0][1] +=1 
    elif direction == 'left':snake[0][0] -=1
    elif direction == 'right':snake[0][0] +=1

    while(msvcrt.kbhit()):
        msvcrt.getch()


    #if key == b'a':
    #    direction = left
    #if key == b'd':
    #    direction = right

    #if key == b'w' or key == b'i':
    #    snake[0][1] -= speed
    #elif key == b's' or key == b'k':
    #    snake[0][1] += speed
    #elif key == b'd' or key == b'l':
    #    snake[0][0] += speed
    #elif key == b'a' or key == b'j':
    #    snake[0][0] -= speed
    #elif key ==b' ':
    #    msvcrt.getch()

    # Snake eat food and teleport to random place
    if snake[0][0] == xfood and snake[0][1] == yfood:
        snake.append([xprev,yprev])    
        score +=1
        xfood = random.randrange(1, width - 2)
        yfood = random.randrange(1, height - 2)
        

        for tail in range(1,len(snake)):
            
            if xfood == snake[tail][0] and yfood == snake[tail][1]:
                xfood = random.randrange(1, width - 2)    
                yfood = random.randrange(1, height - 2)


    if flick == True:
        for tail in range(1,len(snake)):
            xtemp,ytemp = snake[tail]
            snake[tail] = [xprev,yprev]
            xprev,yprev = xtemp,ytemp
            if snake[0] == snake[tail]:
                gameover = True


    print(' SCORE:', score)

    # Snake collision with boundries

    if snake[0][0] == width-1  or snake[0][0] == 0 or snake[0][1] == height-1 or snake[0][1] == 0:
        gameover =True

    
                
                
     

    # --------- String Buffer ---------

    buffer = ""
    
    for i in range(height):
        for j in range(width):
            if j == snake[0][0] and i == snake[0][1]:
                buffer += "\x1b[1m@"  # make bold


            elif j == xfood and i == yfood:buffer += "$"
            elif j == width-1 or j == 0:buffer +="|"
            elif i == height-1 or i == 0:buffer +="-"
            else:
                for k in range(1,len(snake)):
                    if j == snake[k][0]   and i == snake[k][1]: 
                        buffer += "\x1b[0m"  # reset all styles 
                        buffer += "O"
                        break
                else:
                    buffer += " "

                    buffer += "\x1b[0m"    # reset all styles
                
        buffer += "\n"


    print("\033[?25l\033[H", end='')
    print(buffer, end='')
    
    
    
        
    # -------------------------------
