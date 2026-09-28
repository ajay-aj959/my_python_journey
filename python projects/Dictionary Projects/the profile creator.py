
"""
1. The Profile Creator
Task: Create a dictionary named user_profile using standard curly braces {}.
Add the keys: "username" (set to "coder123"), "score" (set to 0), and "premium" (set to False).
Write a line of code to increase the score by 50.
Write another line to change "premium" to True.

"""


userprofile = {
            "username": "coder123",
            "score": 0,
            "premium": False
}



print(userprofile)

userprofile["score"] += 50

userprofile["premium"] = True

print(userprofile)
