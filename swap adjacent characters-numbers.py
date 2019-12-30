'''N=int(input())
N=(input().split()[:N])
L=list(N)
def swap(L):
    if len(L)%2==0:
        L[::2],L[1::2]=L[1::2],L[::2]
        a=' '.join(L)
        return a
    elif len(L)%2==1:
        L.append('"dummy"')
        L[::2], L[1::2] = L[1::2], L[::2]
        L.remove('"dummy"')
        a = ' '.join(L)
        return a
print(swap(L))'''

N=input().split()
a=0
for i in N:
	a=a+int(i)
aa=list(a)
if a==aa[::-1]:
	print("yes")
else:
	print("no")
