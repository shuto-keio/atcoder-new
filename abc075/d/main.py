#!/usr/bin/env python3

from itertools import combinations
import sys
sys.setrecursionlimit(10**6)


n, k = list(map(int, input().split()))

xy = [tuple(map(int, input().split())) for i in range(n)]

# xy.sort()


ans = (10**9*2)**3


# xy = sorted(xy, key=lambda x: x[1])

for r in range(2, 5):
    for data in combinations(xy, r=r):
        x_min = min([i[0] for i in data])
        x_max = max([i[0] for i in data])
        y_min = min([i[1] for i in data])
        y_max = max([i[1] for i in data])
        # print(x_min, x_max, y_min, y_max)
        num = 0
        for i, j in xy:
            # print(i, j)
            if x_min <= i and i <= x_max and y_min <= j and j <= y_max:
                num += 1

        if num >= k:
            ans = min(ans, (x_max-x_min)*(y_max-y_min))

print(ans)
