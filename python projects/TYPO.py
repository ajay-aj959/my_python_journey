
"""
1. manu


        TYPO 
======================

>>  Typng Test
    Game
    Exit

2. typing test



TIME: 00                                            WPM: 00


___________----_____-----___destracive life will not give you productive outcome. 







           RESULTS
=================================
WRONG:      7  
CORRECT:    56 
ACCURACY:   89%
WPM:        32 WPM











3.  game 

                                SCORE:00
-------------------------------------------
|                                         |
|                                         |
|    t                                    |
|                                         |
|                                         |
|           y                             |
|                                         |
|                                         |
|                                    L    |
|                                         |
|                 U                       |
|                                         |
|                                         |
|                                         |
|                                         |
-------------------------------------------




gameover



          GAMEOVER !
    ======================
    SCORE: 73

           Replay? y/n 








"""



import random
import os
import time
import msvcrt




# menu veriables
mainmenu =["Typing Test","Game","Exit"]
key = str()
menu_cursor_lock = 1
menu_cursor = 0
###############################

#typing test variables
paragraph = "Succeeding in any new endeavor requires deep patience, consistent practice, and absolute dedication. Many people expect immediate results, but true mastery takes considerable time to develop properly. When you encounter difficult obstacles, view them as valuable opportunities to learn rather than reasons to quit. Each small mistake you make offers an important lesson that strengthens your overall skills. Keep your primary focus on steady, daily progress instead of demanding immediate perfection. With enough time, your hard work transforms into remarkable achievements. Ultimately, the journey toward reaching a personal goal matters just as much as the final destination."
wrong = []
correct = []
cursor = int()
#typing_Test_key = str()
cursor_speed = 1
timer = 0
count = 59
is_entered = False
WPM = float()
ACCURACY = float()



################################

# game variables
alphabets_string = "UOGgpJFCVYbxtaXwkjQRANDLWsmTSildoceqnMIyhZBPHrvKuEzf"
shoot_timer = 0
shooter = 0
x = 0
width,height = 20,20
word=[]
y= 1
word_clock = 0
Score =int()
highscore_path = "D:/Programming/PYTHON/typo_highscore.txt"
highscore = 0
#################################

# while loop variable
window = 0
gameover = False
##################################
os.system('cls')

while gameover != True:
    time.sleep(0.1)
    buffer = ""

    
    
    # main menu window
    if msvcrt.kbhit():
        if window == 1:
            is_entered =True
        if window == 0:
            key = msvcrt.getch()
            if key == b'\x1b':
                gameover = True
                
        if window == 1:
            key = msvcrt.getch().decode()
            #logic for append worng and correct
            
            if key == text[cursor]:
                correct.append(cursor)
            elif key != text[cursor]:
                wrong.append(cursor)
            cursor+=cursor_speed
                
        if window == 2:
            key = msvcrt.getch().decode()
        if window == 3:
            key = msvcrt.getch().decode()
        if window == 4:
            key = msvcrt.getch().decode()




################################################################

    if window == 0:
        if key == b'\xe0':
            key = msvcrt.getch()
            if key == b'H':
                menu_cursor -= cursor_lock
            elif key == b'P':
                menu_cursor += cursor_lock
        
        if menu_cursor == mainmenu.index("Typing Test") and key == b'\r':
            window = 1
        elif menu_cursor == mainmenu.index("Game") and key == b'\r':
            window = 3
        elif menu_cursor == mainmenu.index("Exit") and key == b'\r':
            gameover = 1

        
        
        # cursor stop
        if menu_cursor <= 0:
            cursor_lock = 0
            menu_cursor = 0
            cursor_lock =1
        elif menu_cursor >=len(mainmenu):
            cursor_lock = 0
            menu_cursor = len(mainmenu)-1
            cursor_lock =1
    
        # cursor print and main menu

        buffer += "   _____T_Y_P_O______\n"
        for menu in range(len(mainmenu)):
            buffer += "\n\t"
            if menu == menu_cursor:
                buffer += "\b\b\b>> "
            buffer += mainmenu[menu]
            buffer += "\n"


        
   
   

    elif window ==1:
        
        if is_entered == True:
            timer +=1
        if timer >= 10:
            timer = 0
            count -=1
        if count <=0:
            count = 0
            curse = True
            window = 2
        
        

        # highlight title 
        buffer += "\t\t\t\t\t\t\t\b\b\b__T_Y_P_I_N_G__T_E_S_T__ \n"
        buffer+= 5*"\n"
        buffer += f"TIME: {count}\n"
        buffer += 138*"="
        buffer += 5*"\n"
       
     #convert string to list
        text = list(paragraph)

        
        # logic 
        for i in range(0,len(wrong)):
            text[wrong[i]] = "~"
        for j in range(0,len(correct)):
            text[correct[j]] = "_"
        for k in range(0,len(text)):
            buffer += text[k]




    

    if window == 2:
        
        """
    you type 313 characters in 1 minute with 2 errors:
    Standard Words: 313 ÷ 5 = 62.6Net Words:
    62.6 - 2 = 60.6WPM: \(60.6 \div 1 = \mathbf{60.6\text{ WPM}}\)


        WPM FORMULA:
        ((total characters / 5)- wrong characters /time in minute)

        ACCURACY FORMULA:
        (Total characters - wrong characters )/total characters *100

        """



        WPM =((len(wrong)+len(correct) /5) - len(wrong) / 1)
        WPM = round(WPM)

        total = len(wrong)+len(correct)
        if total == 0:
            ACCURACY = 100.0
        ACCURACY = (total - len(wrong))/ total * 100

        buffer += "\t\t__R_E_S_U_L_T_S__\n\n"
        buffer += f"\n\t\tWPM:         {WPM}"
        buffer += f"\n\t\tACCURACY:    {ACCURACY:.2f}%"
        buffer += f"\n\t\tWRONG:       {len(wrong)}"
        buffer += f"\n\t\tTotal:       {total}\n"
        
        if key == '\x1b':
            correct.clear()
            wrong.clear()
            is_entered = False
            cursor = 0
            total = 0
            count = 59   
            WPM = 0
            ACCURACY = 0
            key = ""
            window = 0

        






    #window 3 for game 
    elif window == 3:
        
#
 # Score print
        buffer += "\n\n\n"
        buffer += f" \t  SCORE: {Score} \n"
        alphabets = list(alphabets_string)
    
 #      timer for random word from string shooter (0 - 51)
        shoot_timer +=1
        if shoot_timer > 10:
            shooter = random.randrange(0,51)   # get random number between (0 - 51) alphabet
            x = random.randrange(1, 18)    # get random number between (1 - 18)     x cordinate 
            word.append(shooter)          #   alphabet
            word.append(x)                #  x - coordinate
            word.append(y)                #  y - coordinate
            shoot_timer = 0 
    



        for i in range(height):
            for j in range(width):
                   
    
                        
                if i == 0 or i == height-1 :
                    buffer += "-"
                elif j == 0 or j == width-1:
                    buffer += "|"
                else:
                    for k in range(len(word)):
                        if k%3==0:
                            if j == word[k+1] and i == word[k+2]:
                                buffer += alphabets[word[k]]
                                break
                    else :
                        buffer+=" "

    
            buffer += "\n"  
        word_clock +=1
        if word_clock > 4:
            word_clock = 0
    
    
        for m in range(len(word)):
            if m%3 == 2 :
                if  word_clock==4:
                    word[m] +=1
    
    
    
    
    
    
    

        

        for n in range(len(word)):
            if n%3 ==0:
                if alphabets[word[n]] == key:
                    del word[n:n+3]
                    Score +=1
                    break
            
        for end_game in range((len(word))):
            if end_game%3 == 2 :
                if word[end_game] == height:
                    window = 4
    
    
    
        

    elif window == 4:

  

        buffer += f"\t___G_A_M_E____O_V_E_R___\n\n"
        buffer += f"\t  SCORE:              {Score}\n"
        
        if key == '\x1b'and window == 4:
            word.clear()
            Score = 0
            key = ""
            window = 0
            


    # PRINT BUFFER HERE 

    print("\033[2J\033[?25l\033[H",end='')     # clear terminal/hide cursor/move cursor to top-left
    print(buffer,end='')
    