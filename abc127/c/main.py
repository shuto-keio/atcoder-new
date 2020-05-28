#!/usr/bin/env python3

n, m = list(map(int, input().split()))

min_, max_ = 0, 10**5
for i in range(m):
    a, b = list(map(int, input().split()))

    min_ = max(min_, a)
    max_ = min(max_, b)

print(max(max_-min_+1, 0))
