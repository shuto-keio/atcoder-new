#!/usr/bin/env python3
import numpy as np

import sys
sys.setrecursionlimit(10**6)


h, w, n, m = list(map(int, input().split()))
AB = np.array([list(map(int, input().split())) for _ in range(n)], np.int64)
CD = np.array([list(map(int, input().split())) for _ in range(m)], np.int64)

A = AB[:, 0]-1
B = AB[:, 1]-1
C = CD[:, 0]-1
D = CD[:, 1]-1


def count_down(lb):
    mass = lb.copy()
    for row in range(1, mass.shape[0]):
        value = np.maximum(mass[row, :], mass[row-1, :])
        mass[row, :] = np.where(lb[row, :] == -1, -1, value)

    return mass


lb = np.zeros((h, w), np.int64)
lb[A, B] = 1
lb[C, D] = -1

# print(lb)  # normal
# print(lb[::-1]) # upside down
# print(lb[::-1].T) # upside down, left and right reversed
# print(lb[::-1].T) # left and right reversed

lightD = count_down(lb)
lightU = count_down(lb[::-1])[::-1]
lightR = count_down(lb.T).T
lightL = count_down(lb.T[::-1])[::-1].T


ans = ((lightD+lightU+lightR+lightL) > 0).sum()
print(ans)
