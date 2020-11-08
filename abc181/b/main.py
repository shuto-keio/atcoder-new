#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())

ans = 0
for i in range(n):
    a, b = list(map(int, input().split()))

    ans += (a+b)*(b-a+1)//2

print(ans)
