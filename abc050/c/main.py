#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

mod = 10**9+7


def exp2(n):
    ans = 1
    for _ in range(n):
        ans *= 2
        ans %= mod
    return ans


a.sort()

if n == 1:
    if a[0] == 0:
        print(1)
        exit()
    else:
        print(0)
        exit()

if n % 2 == 0:
    for i in range(n):
        if a[i] == (0+i)//2*2+1:
            pass
        else:
            print(0)
            exit()
    print(exp2(n//2))

else:
    for i in range(n):
        if a[i] == (1+i)//2*2:
            pass
        else:
            print(0)
            exit()
    print(exp2(n//2))
