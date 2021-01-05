#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))
abc = [list(map(int, input().split())) for i in range(m)]

d = [[10**10]*n for i in range(n)]

for i in range(n):
    d[i][i] = 0

for a, b, c in abc:
    d[a-1][b-1] = c
    d[b-1][a-1] = c


for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 0
for a, b, c in abc:
    if d[a-1][b-1] != c:
        ans += 1
print(ans)
