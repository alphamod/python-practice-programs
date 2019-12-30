N,K=map(int, input().split())
N=map(int, input().split()[:N])
a=[]
for i in N:
	if i==K:
		a.append(i)
print(len(a)-1)