import math
N,M=map(int, input().split())
if N!=0 and M!=0:
    a=math.gcd(N,M)
    print(a)
else:
    print(-1)
