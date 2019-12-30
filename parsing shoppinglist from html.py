import re
f=open("shoppinglist.html","r")
con=f.read()
a=con.strip().split("\n")
b=[]
c={}
for i in a:
    if "<li>" in i:
        b.append(i)
for j in b:
    item,price=j.split(':')
    it=item.replace('<li>','')
    pr=price.replace('</li>', '')
    c[it.strip()]=pr.strip()
print(c)