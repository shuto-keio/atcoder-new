#!/usr/bin/env python3

n, m = list(map(int, input().split()))

ab = [list(map(int, input().split())) for _ in range(n)]

ab = sorted(ab, key=lambda x: x[0])

ans = 0
for i in range(m):
    a, b = ab[i]
    if b-m >= 0:
        ans += a*m
        print(ans)
        exit()
    else:
        m -= b
        ans += a*b
