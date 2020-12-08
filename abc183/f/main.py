#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.class_info = [{} for i in range(n)]

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
            return x

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        for key, value in self.class_info[y].items():
            if key in self.class_info[x]:
                self.class_info[x][key] += value
            else:
                self.class_info[x][key] = value
        self.class_info[y] = {}

        return x


n, q = list(map(int, input().split()))
c = [i-1 for i in list(map(int, input().split()))]


data = list(range(n))

uf = UnionFind(n)

for i in range(len(c)):
    uf.class_info[i][c[i]] = 1
# print(uf.class_info)

# print(uf.parents)
# print(uf.class_info)
for i in range(q):
    a, b, c = list(map(int, input().split()))

    # print(a, b, c)
    b -= 1
    c -= 1

    if a == 1:
        uf.union(b, c)

    else:
        group_b = uf.find(b)

        if c in uf.class_info[group_b]:
            print(uf.class_info[group_b][c])
        else:
            print(0)

    # print(uf.parents)
    # print(uf.class_info)
