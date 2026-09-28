
"""

Input Data: data = {"id": 101, "temp_code": "X92", "status": "Active"}

Task: Delete the key "temp_code" from 
the dictionary. Ensure that if you run the deletion code 
a second time, it does not crash your program 
(even though the key is already gone).           


"""

import os

data = {
         "id": 101,
         "temp_code": "x92",
         "status": "Active"
}



while True:
    os.system('cls')
    print(f"original:{data}")
    data.pop("temp_code", "none")   # here you have to give  an argument after key delete 'none' or number or value else you will get type error
    print(f"after: {data}")
