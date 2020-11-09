#!/usr/bin/env python3
import numpy as np
import itertools
import sys
sys.setrecursionlimit(10**6)


n = int(input())

n_str = np.array(list(str(n)))

for i in reversed(range(1, len(n_str)+1)):
    for a in itertools.combinations(range(0, len(n_str)), i):
        num = np.take(n_str, a)
        num = int(''.join(num))
        if num % 3 == 0:
            print(len(n_str)-i)
            exit()
print(-1)
