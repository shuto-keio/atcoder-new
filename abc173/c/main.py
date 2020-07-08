#!/usr/bin/env python3

import itertools
import numpy as np

h, w, k = list(map(int, input().split()))

c = [list(str(input())) for _ in range(h)]
# print(c)

c = np.array(c)

ans = 0
for h_flag in itertools.product([0, 1], repeat=h):
    h_flag = [i for i, j in enumerate(h_flag) if j == 1]
    for w_flag in itertools.product([0, 1], repeat=w):
        w_flag = [i for i, j in enumerate(w_flag) if j == 1]
        # print()
        c_ = c[:]
        c_ = np.take(c_, h_flag, axis=0)
        # print(c_)
        c_ = np.take(c_, w_flag, axis=1)
        # print(c_)

        if np.sum(c_ == "#") == k:
            ans += 1

print(ans)
