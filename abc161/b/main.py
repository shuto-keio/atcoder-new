#!/usr/bin/env python3

import numpy as np
N, M = map(int, input().split())
A = list(map(int, input().split()))

A = np.array(A)

num = np.sum(A >= np.sum(A)/(4*M))

if num >= M:
    print("Yes")
else:
    print("No")
