#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))

data1 = set([])
data2 = set([])
for i in range(m):
    a, b = list(map(int, input().split()))
    if a == 1:
        data1.add(b)
    if b == 1:
        data1.add(a)
    if a == n:
        data2.add(b)
    if b == n:
        data2.add(a)

if len(data1 & data2) >= 1:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
