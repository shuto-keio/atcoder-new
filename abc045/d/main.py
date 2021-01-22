#!/usr/bin/env python3
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
h, w, n = list(map(int, input().split()))

data = defaultdict(int)
for i in range(n):
    a, b = list(map(int, input().split()))
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if a+y >= 2 and a+y <= h-1 and b+x >= 2 and b+x <= w-1:
                data[(a+y, b+x)] += 1
    # print(data)

# print(data)

data2 = defaultdict(int)
for key, value in data.items():
    if value <= 10:
        data2[value] += 1

print((w-2)*(h-2)-len(data))
for i in range(1, 10):
    print(data2[i])
