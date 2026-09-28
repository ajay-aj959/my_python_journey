"""
Your Task:
Use dict.fromkeys() to create a new dictionary called game_board.
Pass the coordinates list as the keys.
Set the default starting value for every single key to a simple dot string: "." (this represents an empty space on the board).
Print game_board at the end

"""


coordinates = ["A1", "A2", "A3", "B1", "B2", "B3"]

game_board = dict.fromkeys(coordinates, ".")
print(game_board)

