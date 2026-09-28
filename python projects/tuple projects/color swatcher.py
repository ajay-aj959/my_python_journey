"""

1. create fun rgb_to_hex(create tuple)
2. unpack tuple
3. return f"#{r:02x}-- close function
4. get three seperate input
5. pack input into single tuple
6. pass tuple into rbg_to_hex function 
7.print output in formating string

"""

def rgb_to_hex(color_tuple):
    r,g,b = color_tuple
    return f"#{r:02x}{g:02x}{b:02x}"

red_input= int(input("red(0-255):"))
green_input= int(input("gree(0-255):"))
blue_input= int(input("blue(0-255):"))

user_color = (red_input,green_input,blue_input)

hex_result = rgb_to_hex(user_color)

print(f"user input:{user_color}")
print(f"hex_result:{hex_result}")









