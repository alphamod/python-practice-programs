import webbrowser
def signin():
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
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            message='''<html>
            <title>Welcome</title>
            <body bgcolor="blue">
            <h1>Welcome '''+uname+'''</h1>
            </body>
            </html>'''
            wfile.write(str(message))
            wfile.close()
            webbrowser.get(chrome_path).open("welcome.html")

        else:
            print("Password is incorrect.")
    else:
        print("Username is incorrect")
signin()