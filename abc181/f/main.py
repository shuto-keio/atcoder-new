#!/usr/bin/env python3
from math import sqrt
import sys
sys.setrecursionlimit(10**6)

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

# print(xy_p)
# print(xy_m)
# xy_p.sort()
# xy_m.sort()


def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2


edges = []

S = n
T = n+1

for i in range(n):
    edges.append(((100-points[i][1])**2, i, S))
    edges.append(((100+points[i][1])**2, i, T))
    for j in range(i+1, n):
        edges.append((dist(points[i], points[j]), i, j))

edges.sort()
# print(edges)
p = list(range(n+2))


def r(x):
    if p[x] == x:
        return x
    p[x] = r(p[x])
    return p[x]


def merge(x, y):
    x = r(x)
    y = r(y)
    if x == y:
        return
    p[x] = y


def same(x, y):
    return r(x) == r(y)


for (length, x, y) in edges:
    merge(x, y)
    if same(S, T):
        print("%.10f" % (sqrt(length)/2))
        exit()
