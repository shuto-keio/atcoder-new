#!/usr/bin/env python3


n, k = list(map(int, input().split()))
h = [int(input()) for _ in range(n)]

h.sort(reverse=True)

ans = 10**10
for i in range(0, n-k+1):
    max_ = h[i]
    min_ = h[i+k-1]
    ans = min(ans, max_-min_)
print(ans)
