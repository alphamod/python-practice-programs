import re
file=open("shoppinglist.html")
a=file.read()
b=re.findall(r'</\w+>', a)
c=re.findall(r'<\w+.>', a)
if len(b)==len(c):
    print("the html file is balanced")
else:
    print("the html file is not balanced")
