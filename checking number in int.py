num=12345
v=int(input("enter the check number"))
while (num!=0):
    remainder=int(num%10)
    if (remainder == v):
        print("yes")
        break
    num = int(num / 10)
else:
    print("not found")
