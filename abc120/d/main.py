#!/usr/bin/env python3
import numpy as np

n, m = list(map(int, input().split()))

ab = [list(map(int, input().split())) for _ in range(m)]
ab.reverse()


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


tree = UnionFind(n)
buf = [n*(n-1)//2]
for i in range(len(ab)-1):
    a, b = ab[i]
    a, b = a-1, b-1
    if tree.same(a, b):
        buf.append(buf[-1])
        continue
    ra = tree.parents[tree.find(a)]
    rb = tree.parents[tree.find(b)]
    buf.append(buf[-1] - ra * rb)
    tree.union(a, b)

buf.reverse()
# ans = []
# roots = [-x for i, x in enumerate(tree.parents) if x < 0]
# roots = np.array(roots)
# ans_tmp = n*(n-1)//2-np.sum(roots*(roots-1))//2
# ans.append(ans_tmp)
# for a, b in reversed(ab):
#     tree.union(a-1, b-1)
#     roots = [-x for i, x in enumerate(tree.parents) if x < 0]
#     roots = np.array(roots)
#     ans_tmp = n*(n-1)//2-np.sum(roots*(roots-1))//2
#     ans.append(ans_tmp)

print('\n'.join(map(str, buf)))
