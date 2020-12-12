#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
p = [i-1 for i in list(map(int, input().split()))]

ans = 0
for i in range(0, len(p)-1):
    if p[i] == i:
        p[i], p[i+1] = p[i+1], p[i]
        ans += 1

if p[-1] == (len(p)-1):
    ans += 1

print(ans)
