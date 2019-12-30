class codekata():
    f=open("codekata_ques.txt", 'r')
    b=f.read()
    c=b.split('\n')
    geekoins=0
    d={}
    for i in c:
        num,ques=i.split(',')
        d[num.strip()]=ques.strip()
    def choice(self):
        self.userchoice = input("Enter Easy, Medium or Hard.\nEnter Here: ")
        codekata().welcome()

    def welcome(self):
        if self.userchoice=='Easy' or 'easy' or 'EASY':
            pass
            #easy question func
        elif self.userchoice=='medium' or 'Medium' or 'MEDIUM':
            pass
            #Medium choice ques
        elif self.userchoice=='Hard' or 'hard' or 'HARD':
            pass
            #hard ques func
        else:
            print("invalid input. Try again.")
            codekata.choice()
    def getEasyQues(self):

        pass


a=codekata()
a.choice()
print(a.userchoice)