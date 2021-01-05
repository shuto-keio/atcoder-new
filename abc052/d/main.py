#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)


n, a, b = list(map(int, input().split()))
x = list(map(int, input().split()))

ans = 0
for i in range(1, len(x)):
    dis = x[i]-x[i-1]
    ans += min(b, a*dis)
print(ans)
