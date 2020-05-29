#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, q = list(map(int, input().split()))

tree = [[] for _ in range(n)]
for i in range(n-1):
    a, b = list(map(int, input().split()))
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

add = [0]*n
for _ in range(q):
    p, x = list(map(int, input().split()))
    add[p-1] += x

ans = [0] * n


def dfs(v, p, value):  # p: parent of v
    value += add[v]
    ans[v] = value
    for c in tree[v]:
        if c == p:
            continue
        dfs(c, v, value)


dfs(0, -1, 0)

# print(add)

print(*ans)
