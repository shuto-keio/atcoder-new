#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0
if a[0] > x:
    ans += a[0]-x
    a[0] = x

for i in range(len(a)-1):
    if a[i]+a[i+1] > x:
        diff = (a[i]+a[i+1])-x
        ans += diff
        a[i+1] -= diff


print(ans)
