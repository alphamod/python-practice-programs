x = range (3,12)
a=0
b=0
s=0
for n in x:
    s=s+n
    if (n%2==0):
        a= a+5+n
    else:
        b=b+15+n
print("total sum is", s)
print(a, "is sum of 5 plus element")
print(b, "is sum of 15 plus element")


