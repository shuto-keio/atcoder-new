#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

k, s = list(map(int, input().split()))

ans = 0
for i in range(0, k+1):
    for j in range(0, k+1):
        # print(i, j)
        if s-(i+j) <= k and s-(i+j) >= 0:
            ans += 1

print(ans)
