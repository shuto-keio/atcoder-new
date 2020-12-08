#!/usr/bin/env python3
from itertools import permutations
import sys
sys.setrecursionlimit(10**6)


n, k = list(map(int, input().split()))
t = [list(map(int, input().split())) for i in range(n)]

ans = 0
for i in permutations(range(1, n), r=n-1):
    t_tmp = 0
    # print(i)
    t_tmp += t[0][i[0]]
    # print(0, i[0], t[0][i[0]])
    for j in range(1, len(i)):
        t_tmp += t[i[j-1]][i[j]]
        # print(i[j-1], i[j], t[i[j-1]][i[j]])
    t_tmp += t[i[-1]][0]
    # print(i[-1], 0, t[i[-1]][0])
    if t_tmp == k:
        ans += 1
print(ans)
