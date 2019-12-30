import operator, functools
N=int(input())
N=map(int, input().split()[:N])
a=functools.reduce(operator.and_, N)
print(a)
