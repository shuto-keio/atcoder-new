#!/usr/bin/env python3

import itertools

n = int(input())

ab = [list(map(int, input().split())) for i in range(n)]


sum_dis = 0
for i, j in itertools.combinations(range(n), 2):
    x1, y1 = ab[i]
    x2, y2 = ab[j]
    sum_dis += ((x1-x2)**2+(y1-y2)**2)**0.5

sum_dis /= n*(n-1)/2

print(sum_dis*(n-1))
