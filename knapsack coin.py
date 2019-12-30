N,S=map(int, input().split())
n=N
N=map(int, input().split()[:N])
V=list(N)
V.sort(reverse=True)
L=[]
for i in range (0,n):
    while S>=V[i]:
        S=S-V[i]
        L.append(V[i])
print(len(L))