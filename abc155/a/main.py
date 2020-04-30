#!/usr/bin/env python3

import itertools

degit = list(map(int, input().split()))

flag = 0
for i, j, k in itertools.permutations(degit, 3):
    if i == j:
        if j != k:
            flag = 1
    else:
        if j == k:
            flag = 1
    # print(i, j, flag)


print("Yes" if flag == 1 else "No")
