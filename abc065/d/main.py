#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)


n = int(input())

x_list = []
y_list = []
xy_list = []
for i in range(n):
    x, y = list(map(int, input().split()))
    x_list.append([i, x])
    y_list.append([i, y])
    xy_list.append([i, (x, y)])

x_list = sorted(x_list, key=lambda x: x[1])
y_list = sorted(y_list, key=lambda x: x[1])

edges = []
# for i in range(n):
#     edges[i] = {}

for i in range(len(x_list)-1):
    index_pre, pos_pre = x_list[i]
    index_post, pos_post = x_list[i+1]
    dis = abs(pos_pre-pos_post)
    edges.append([(index_pre, index_post), dis])
    # edges.append([(index_post, index_pre), dis])

for i in range(len(y_list)-1):
    index_pre, pos_pre = y_list[i]
    index_post, pos_post = y_list[i+1]
    dis = abs(pos_pre-pos_post)
    edges.append([(index_pre, index_post), dis])
    # edges.append([(index_post, index_pre), dis])

edges = sorted(edges, key=lambda x: x[1])


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


uf = UnionFind(n)
ans = 0
for (i, j), dis in edges:
    if uf.find(i) == uf.find(j):
        continue
    else:
        uf.union(i, j)
        ans += dis
print(ans)
