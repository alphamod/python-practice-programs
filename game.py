yes=["Yes", "yes", "YES", "y", "Y"]
no=["No", "no", "NO", "N", "n"]
user_input=input("Do you want to continue with the game?: ")
for i in yes:
    if (i==user_input):
        print("Enjoy the game!!!")
for i in no:
    if (i==user_input):
        print("Quitting Game.")
else:
    print("invalid input")