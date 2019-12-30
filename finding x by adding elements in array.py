'''N, X = map(int, input().split())
n = N
N = map(int, input().split()[:N])
l=list(N)
a = 0
for i in range(n):
    for x in l:
        a = x + a
        if a == X:
            print("yes")
            break
        else:
            a = 0
    if a != X:
        print("no")
'''
