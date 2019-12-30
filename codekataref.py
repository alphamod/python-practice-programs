class codekata:
    usip=input("Enter Easy Medium or Hard: ")
    file=open('codekata.txt', 'r')
    a=file.read()
    b=a.split('\n')
    d={}
    ans1=''
    ans2=''
    ans3=''
    testcase1='answer1'
    testcase2='answer2'
    testcase3='answer3'
    g1=100
    g2=200
    g3=300
    for i in b:
        num,ques=i.split(':')
        d[num.strip()]=ques.strip()

    def choice(self):
        if self.usip=='E':
            self.ans1=input(self.d['1'])
            codekata().checkans1()
        elif self.usip=='M':
            self.ans2=input(self.d['2'])
            codekata().checkans2()
        elif self.usip==('H'):
            self.ans3=input(self.d['3'])
            codekata().checkans3()
        else:
            print('invalid input. Try again with Capslock')
            self.usip=input("Enter E for Easy, M for Medium or H for Hard: ")
            codekata().choice()

    def checkans1(self):
        if self.ans1==self.testcase1:
            print("Congratulations!", self.g1,'geekoins has been added to your profile' )
        else:
            print('invalid answer. Test case failed')

    def checkans2(self):
        if self.ans2==self.testcase2:
            print("Congratulations!", self.g2, 'geekoins has been added to your profile')
        else:
            print('invalid answer. Test case failed')

    def checkans3(self):
        if self.ans3==self.testcase3:
            print("Congratulations!", self.g3, 'geekoins has been added to your profile')
        else:
            print('invalid answer. Test case failed')
a=codekata()
a.choice()
a.file.close()
