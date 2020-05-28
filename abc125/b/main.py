#!/usr/bin/env python3
import numpy as np

n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

v = np.array(v)
c = np.array(c)

ans = np.sum((v-c)*((v-c) >= 0))

print(ans)
