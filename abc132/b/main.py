#!/usr/bin/env python3

n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(1, len(p)-1):
    min_ = min(p[i-1], p[i], p[i+1])
    max_ = max(p[i-1], p[i], p[i+1])
    if p[i] != min_ and p[i] != max_:
        count += 1
print(count)
