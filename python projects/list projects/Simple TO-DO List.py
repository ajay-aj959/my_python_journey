"""
stpes
1.display menu
2.movement
3.boundry handling
4.enter selection 
5.exit
6.only than add /remove /view/change


===================
    TO-DO LIST
===================
> Add task
  View task
  Remove task 
  Change task
  Exit


"""




import os
import msvcrt
import time


menu =["Add Task","View Task","Remove Task","Change Task","Exit"]
task =["","wakeup","brush teeth","gym","breakfast","meeting"]
cursor = 0
key = 0
todo_loop = 0
os.system('cls')

while todo_loop != 1:
    
   
    buffer = ""
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'\xe0':
            key = msvcrt.getch()
                       
            if key == b'H':
                cursor -=1
            elif key ==b'P':
                cursor +=1
        
        if key == b'\r':
                    if cursor == 0:
                        task.append(input("New Task \n"))
                    elif cursor == 1:
                        for view in range(1,len(task)):
                            print(view,task[view])
                        msvcrt.getch()
                    elif cursor == 2:
                        for view in range(1,len(task)):
                            print(view,task[view])
                        rem = input("enter task : ")
                        task.remove(rem)
                    elif cursor == 3:
                        for view in range(1,len(task)):
                            print(view,task[view])
                        old_task = input("Enter Old Task: ")
                        new_task = input("Enter New Task: ")
                        index = task.index(old_task)
                        task[index] = new_task
                    elif cursor == 4:
                        todo_loop = 1
             

    

    if cursor < 0:
        cursor = 0
    elif cursor > 3:
        cursor = 4


   
    for i in range(len(menu)):
        if cursor == i:
            buffer +="> "
        buffer += menu[i]
        buffer += "\n"

    print("\033[2J\033[H", end="")
    print("*****TO-DO LIST*****")
    print(buffer,end='')  
    time.sleep(0.1)  
        
    
    
    