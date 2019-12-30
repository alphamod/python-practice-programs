c=int(input("enter the start range"))
d=int(input("enter the end range"))
x = range (c,d)
a=1
b=1
for n in x:
    if (n%2==0):
        a= a*n
    else:
        b=b*n
print(a, "is product of even numbers from the range", c, "to", d)
print(b, "is product of odd numbers from the range", c, "to", d)


