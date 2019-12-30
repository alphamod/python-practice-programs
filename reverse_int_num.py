num=87645
rev_num=0
while (num>0):
    rem=num%10
    rev_num=rev_num*10+rem
    num=int(num/10)
print("the reversed number is", rev_num)


