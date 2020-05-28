#!/usr/bin/env python3

import itertools
import numpy as np

n, m = list(map(int, input().split()))

ks = [list(map(int, input().split())) for _ in range(m)]

p = np.array(list(map(int, input().split())))

# print(ks)
ans = 0
for i in itertools.product([0, 1], repeat=n):
    i = np.array(i)
    flag = 1

    for j in range(len(ks)):
        ks_tmp = np.array(ks[j])
        if np.sum(np.take(i, ks_tmp[1:]-1)) % 2 == p[j]:
            continue
        else:
            flag = 0
            break
    if flag == 1:
        ans += 1

print(ans)
