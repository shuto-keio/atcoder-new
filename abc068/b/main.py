#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())

ans = 0
for i in range(1, n+1):
    tmp = 0
    while(i % 2 == 0):
        if i % 2 == 0:
            tmp += 1
            i //= 2
    ans = max(ans, tmp)
print(2**ans)
