#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

x, y = list(map(int, input().split()))

ans = 0
num = x
while(num <= y):
    ans += 1
    num *= 2
print(ans)
