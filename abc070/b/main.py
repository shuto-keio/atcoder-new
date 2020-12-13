#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)


a, b, c, d = list(map(int, input().split()))

ans = 0
for i in range(0, 101):
    if a <= i and i < b:
        if c <= i and i < d:
            ans += 1
print(ans)
