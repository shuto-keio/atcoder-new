#!/usr/bin/env python3


n, m = list(map(int, input().split()))
h = list(map(int, input().split()))

best = [1 for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    if h[a-1] <= h[b-1]:
        best[a-1] = 0
    if h[b-1] <= h[a-1]:
        best[b-1] = 0

# print(best)
print(sum(best))
