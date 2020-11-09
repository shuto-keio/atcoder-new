#!/usr/bin/env python3
import numpy as np
import sys
sys.setrecursionlimit(10**6)


n = int(input())
a = list(map(int, input().split()))

data = [0]*1000
for i in range(1, 1000):
    for j in a:
        if j % (i+1) == 0:
            data[i] += 1
# print(data)
print(np.argmax(data)+1)
