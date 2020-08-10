#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))

a = [j-(i+1) for i, j in enumerate(a)]

a.sort()

b = a[n//2]

ans = 0
for i in a:
    ans += abs(i-b)

print(ans)
