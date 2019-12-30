import re
import webbrowser
class username:
    yes=["Yes", "yes", "YES", "y", "Y"]
    no=["No", "no", "NO", "N", "n"]
    spec=['!','@', '#', '$','%','^', '&', '*', '(', ')', ':', ',', '[',']','=', '-','_', '+' ]


    def signup(self):
        def nuser(self):
            newuserip=input("Enter the new Username: ")
            if re.match(r'\w@\w\.a-z', newuserip):
                newuser=newuserip
            else:
                print("Username is not valid email")


        def npass(self):#Getting new password with at least one  special char, digit and upper and lower case
            newpassip = input("Enter the new password: ")
            newpassipc= input("Confirm new password: ")
            if newpassip==newpassipc:
                if any(x.isupper() for x in newpassip):
                    if any(x.islower() for x in newpassip):
                        if any(x.isdigit() for x in newpassip):
                            if 6<len(newpassip)<15:
                                if any(x==self.spec[i] for i in range(len(self.spec)) for x in newpassip):
                                    newpass=newpassip
                                else:
                                    print("Password must contain a special character")
                            else:
                                print("Password length must be min of 6 char and max of 15 char.")
                        else:
                            print("Password must contain a numeric digit")
                    else:
                        print("Password must contain a lower case character")
                else:
                    print("Password must contain a upper case character")
            else:
                print("Passwords do not match")

        if username().signup().nuser().newuser in username().signin().usp:
            print("username already exists! Select a different user name. Try different username or sign in")
            sip=input("Enter y to sign in")
            if sip==('y' or 'Y'):
                username().signin()
            else:
                nuser()
        else:
            npass()
            newuser=username().signup().nuser().newuser.strip()
            nfile=open("user.txt", 'a')
            nfile.write('\n')
            nfile.write(str(newuser+':'+username().signup().npass().newpass))
            print("Congratulations!! Your Account has been created")
            print("Please Sign in.")
            username().signin()
            nfile.close()

    def signin(self):
        file = open("user.txt", "r+")
        a=file.read()
        b=a.split("\n")
        usp={}
        for i in b:
            user,pwd=i.strip().split(":")
            #print(user,pwd)
            usp[user.strip()]=pwd.strip()
        uname=input("Enter the Username: ")
        pword=input("Enter the Password: ")
        if uname in usp:
            if usp[uname]==pword:
                print("You have successfully logged in")
                wfile=open("welcome.html", "w")
                chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                message='''<html>
                <title>Welcome</title>
                <body>
                <h1>Welcome <i>'''+uname+'''</i></h1>
                </body>
                </html>'''
                wfile.write(str(message))
                wfile.close()
                webbrowser.get(chrome_path).open("welcome.html")
            else:
                print("Password is incorrect.")
        else:
            print("Username is incorrect")
            user_input=input("Would you like to signup as a new User?")
            for i in self.yes:
                if (i == user_input):
                    username().signup()
            for i in self.no:
                if (i == user_input):
                    print("Have a great day!!!")
            else:
                print("invalid input")
            file.close()

a=username()
a.signin()