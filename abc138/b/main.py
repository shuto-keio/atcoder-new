#!/usr/bin/env python3

import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))

ans = 0

print(1/np.sum(1/a))
