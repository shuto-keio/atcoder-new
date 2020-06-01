#!/usr/bin/env python3

import numpy as np

n, m, c = list(map(int, input().split()))
b = np.array(list(map(int, input().split())))


ans = 0
for i in range(n):
    a = np.array(list(map(int, input().split())))
    if np.sum(a*b)+c > 0:
        ans += 1
print(ans)
