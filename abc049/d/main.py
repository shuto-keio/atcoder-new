#!/usr/bin/env python3
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
n, k, l = list(map(int, input().split()))
pq = [list(map(int, input().split())) for i in range(k)]
rs = [list(map(int, input().split())) for i in range(l)]


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())


road = UnionFind(n)
rail = UnionFind(n)


for p, q in pq:
    p -= 1
    q -= 1
    road.union(p, q)


for r, s in rs:
    r -= 1
    s -= 1
    rail.union(r, s)

data = defaultdict(int)
for i in range(n):
    p_road = road.find(i)
    p_rail = rail.find(i)
    data[(p_road, p_rail)] += 1
    # print((p_road, p_rail))
# print(data)

ans = []
for i in range(n):
    p_road = road.find(i)
    p_rail = rail.find(i)
    # print(p_road)
    ans.append(data[(p_road, p_rail)])

print(*ans)
