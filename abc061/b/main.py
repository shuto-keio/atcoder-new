#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))
data = [[] for i in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    data[a].append(b)
    data[b].append(a)


for i in range(len(data)):
    print(len(data[i]))
