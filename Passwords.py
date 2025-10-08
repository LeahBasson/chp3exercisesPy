# Code a function that returns a boolean if the entered password is correct.
# Maximum of three times.
# Add another function. This function asks the user to input the password.

def confirmation(pwd="None"):
    if ent_pwd == "Leah20":
        return True
    else:
        return False

for count in range(3):
    ent_pwd = input("Enter password (3 attempts): ")
    pwd = confirmation(ent_pwd)
    print(pwd)

def confirm():
    ent_pwd = input("Enter password (3 attempts): ")
    return ent_pwd

confirm()