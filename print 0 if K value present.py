N,K=map(int, input().split())
N=map(int, input().split()[:N])
for i in N:
    if (i==K):
        print("yes")
        break
else:
    print("no")

