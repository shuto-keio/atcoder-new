#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = [list(map(int, input().split())) for i in range(m)]

ans = sum(t)

for p, x in px:
    diff = t[p-1]-x
    print(ans-diff)

# print(ans-diff)
