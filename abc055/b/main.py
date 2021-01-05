#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())

mod = 10**9+7

ans = 1
for i in range(n):
    ans *= (i+1)
    ans %= mod

print(ans)
