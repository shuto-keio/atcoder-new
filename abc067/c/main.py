#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

sum_a = sum(a)

sunuke = 0
kuma = sum_a

ans = 10**10
for i in range(0, n-1):
    sunuke += a[i]
    kuma = sum_a - sunuke
    ans = min(ans, abs(kuma-sunuke))

print(ans)
