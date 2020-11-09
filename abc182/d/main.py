#!/usr/bin/env python3

import numpy as np
import sys
sys.setrecursionlimit(10**6)


n = int(input())
a = list(map(int, input().split()))

data = np.cumsum(a)
data_max = 0
data2 = []
for i in data:
    data_max = max(i, data_max)
    data2.append(data_max)
# print(data)
# print(data2)

ans = 0
now = 0
for i in range(len(data)):
    ans_tmp = now+data2[i]
    ans = max(ans, ans_tmp)
    now += data[i]

print(ans)
