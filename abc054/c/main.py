#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(m)]

path = [[] for i in range(n)]
for a, b in ab:
    path[a-1].append(b-1)
    path[b-1].append(a-1)


history = set([0])


def dfs(now):
    if len(history) == n:
        return 1
    ans = 0
    route = path[now]
    for i in route:
        if i not in history:
            history.add(i)
            ans += dfs(i)
            history.remove(i)
    return ans


ans = dfs(0)

print(ans)
