#!/usr/bin/env python3

import numpy as np

n = int(input())
x_y = [list(map(int, input().split())) for _ in range(n)]

xy = [i+j for i, j in x_y]

ans1 = max(xy)-min(xy)


xy_rev = [i-j for i, j in x_y]
min_index = np.argmin(xy_rev)
max_index = np.argmax(xy_rev)

x1, y1 = x_y[max_index]
x2, y2 = x_y[min_index]

ans2 = abs(x2-x1)+abs(y2-y1)

print(max(ans1, ans2))
