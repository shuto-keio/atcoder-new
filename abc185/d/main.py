#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))

if m == 0:
    print(1)
    exit()

else:
    a = list(map(int, input().split()))

    a.sort()

    if a[0] != 1:
        a = [0]+a
    if a[-1] != n:
        a.append(n+1)

    k = 10**10
    for i in range(len(a)-1):
        tmp = (a[i+1]-a[i])-1
        if tmp != 0:
            k = min(k, tmp)

    # print(k)
    ans = 0
    for i in range(len(a)-1):
        tmp = (a[i+1]-a[i])-1
        if tmp != 0:
            ans += tmp//k
            if tmp % k != 0:
                ans += 1

    print(ans)
