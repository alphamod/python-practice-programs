class mstring():
    al="user:pwd.1234:456 y65."

    def mysplit(self,a):
        if a in self.al:
            x=self.al.split(a)
            print(x)
        else:
            print('-1')

    '''def mysplit(self):
        count = 0
        for i in self.al:
            if i == ":":
                print(self.al.split(i))
                break
            else:
                count+=1
        if count == len(self.al):
            print("-1")'''

    def myfind(self,y):
        if y in self.al:
            d=self.al.find(y)
            print(d)
        else:
            print('-1')

l=mstring()
l.mysplit(':')
l.myfind('.')