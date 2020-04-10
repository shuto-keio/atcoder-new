#!/usr/bin/env python3

import collections

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)
values = c.keys()
counts = c.values()

subs = {}
a_sum = 0
for v, c in zip(values, counts):
    subs[v] = c
    a_sum += (c * (c-1)) // 2

for i in range(N):
    print(a_sum - subs[A[i]] + 1)
