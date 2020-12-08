#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)


n, w = list(map(int, input().split()))


data = [0] * (2*10**5 + 1)


for i in range(n):
    s, t, p = list(map(int, input().split()))
    data[s] += p
    data[t] -= p


for i in range(1, len(data)):
    data[i] += data[i-1]

if max(data) <= w:
    print("Yes")
else:
    print("No")
