N=int(input())
N=map(int, input().split()[:N])
a=0
for i in N:
	a= (i | a)
print(a)