import msvcrt

key = 0
while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        print(key)