'''file=open("previous week.csv", 'r')
a=file.read()
b=a.split('\n')
#print(b)
d={}
ab=b[0].split(',')
for i in ab:
    d[i]=''
print(d)
max_cod_score=[]
for i in b[1:]:
    for j in i:

'''

'''a=input("Enter the number: ")
a=list(a)
c=[]
d=[]
for i in a:
    if int(i)%2==0:
        c.append(i)
    elif int(i)%2!=0:
        d.append(i)
print("the total odd numbers are ", len(d))
print("the total even numbers are ", len(c))
'''

guvi='guvigeek'

for i in range(guvi):
    print(i)