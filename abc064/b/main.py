#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = 0
for i in range(1, n):
    ans += a[i]-a[i-1]
print(ans)
