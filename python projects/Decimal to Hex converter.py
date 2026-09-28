


base16 = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
hex_value = []
decimal = int(input("decimal: ")) # 255   ---- FF
remainder = 0

while decimal > 0:  # loop will run until decimal > 0
    remainder = decimal % len(base16) 
    #1. remainder =  255 % 16 --- remainder = 15
    #2. last remainder = 15

    decimal = decimal // len(base16)
    #1. decimal = 255 // 16 = 15
    #2. decimal = 15 // 16 = 0


    hex_value.append(base16[remainder])
    #1. 15---base16 --- hex_value[F]
    #2. 15---base16 --- hex_value[F]

    #1. decimal = 15 still > 0
    #2. decimal = 0  terminate loop 

for i in range(1,len(hex_value)+1):
    print(hex_value[-i],end='')



    