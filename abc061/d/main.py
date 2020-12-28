#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))

# data = [[] for i in range(n)]
edges = []
for i in range(m):
    a, b, c = list(map(int, input().split()))
    edges.append((a-1, b-1, -c))


map_ = [float('inf')] * n
map_[0] = 0
for i in range(n):
    if i == n-1:
        old = map_[-1]

    for a, b, c in edges:
        if map_[b] > map_[a] + c:
            map_[b] = map_[a] + c

if old == map_[-1]:
    print(-map_[-1])
else:
    print("inf")
