#!/usr/bin/env python3

# Union Findデータ構造


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
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n, m, k = map(int, input().split())

group = UnionFind(n)

friends_num = [0 for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    group.union(a, b)
    friends_num[a] += 1
    friends_num[b] += 1

block_list = [[] for _ in range(n)]
for i in range(k):
    c, d = map(int, input().split())
    c, d = c-1, d-1
    block_list[c].append(d)
    block_list[d].append(c)

# print(friends_dict)
# print(block_dict)

for i in range(group.n):
    count = group.size(i) - 1 - friends_num[i]
    for j in block_list[i]:
        if j in block_list[i]:
            if group.same(i, j):
                count -= 1

    print(count, "", end="")
