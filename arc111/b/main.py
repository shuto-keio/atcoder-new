#!/usr/bin/env python3
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)


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

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]

uf = UnionFind(4*10**5+1)
data = defaultdict(int)
for a, b in ab:
    a -= 1
    b -= 1
    data[a] += 1
    data[b] += 1
    uf.union(a, b)

ans = 0
for key, value in uf.all_group_members().items():
    v = len(value)
    e = 0
    for i in value:
        e += data[i]
    e //= 2
    ans += min(e, v)

print(ans)
