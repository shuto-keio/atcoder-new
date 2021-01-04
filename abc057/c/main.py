#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
n = int(input())

data = set()
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        data.add(i)

min_ = 10**10
for i in data:
    j = n//i
    # print(i, j)
    min_ = min(min_, max(len(str(i)), len(str(j))))

print(min_)
