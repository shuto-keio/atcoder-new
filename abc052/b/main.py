#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
s = list(str(input()))

ans = 0
now = 0
for i in s:
    if i == "I":
        now += 1
    else:
        now -= 1
    ans = max(ans, now)

print(ans)
