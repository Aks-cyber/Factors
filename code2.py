# 24 = [1,2,3,4,6,8,12,24] prime=[1,2,3]

# n = 24, T.C = 0(n) = 24

# n = 24, T.C = root(n) = 4.89

from math import *
def func1(n):
    # T.C = 0(n)
    div1 = []
    for i in range(1,n+1): #[1,n]
        if n % i == 0:
            div1.append(i)
    return div1

def func2(n):
    # T.C = root(n)
    for i in range(1,int(sqrt(n)+1)): #[1,root(n)]
        div2 = set()
        if n % i == 0:
            div2.add(i)
            div2.add(n%i)
    return list(div2)

t = int(input())
while t:
    n = int(input())
    div1 = func1(n)
    print(*div1)
    div2 = func2(n)
    print(*div2)
    t = t-1
