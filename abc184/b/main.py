#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)


n, x = list(map(int, input().split()))
s = list(str(input()))

for i in s:
    if i == "x":
        x = max(x-1, 0)
    else:
        x += 1
print(x)
