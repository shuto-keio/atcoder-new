#!/usr/bin/env python3


def main():
    n, m = list(map(int, input().split()))
    p = [i-1 for i in list(map(int, input().split()))]

    uf = UnionFind(n)
    for i in range(m):
        x, y = list(map(int, input().split()))
        uf.union(x-1, y-1)

    roots = uf.roots()
    sets_dict = {}
    members_dict = {}
    for i in roots:
        sets_dict[i] = set([])
        members_dict[i] = set([])

    for i in range(n):
        root = uf.find(i)
        sets_dict[root].add(p[i])
        members_dict[root].add(i)
        # print(i, root)
    # print(sets_dict)
    # print(members_dict)
    ans = 0
    for i in roots:
        ans += len(sets_dict[i] & members_dict[i])
    print(ans)


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


if __name__ == "__main__":
    main()
