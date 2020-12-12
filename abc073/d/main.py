#!/usr/bin/env python3
from itertools import permutations
import sys
sys.setrecursionlimit(10**6)

n, m, r_ = list(map(int, input().split()))

r = [i-1 for i in list(map(int, input().split()))]

data = [[10**10]*n for i in range(n)]
for i in range(m):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    data[a][b] = c
    data[b][a] = c


for k in range(n):
    for i in range(n):
        for j in range(n):
            dis1 = data[i][j]
            dis2 = data[i][k]+data[k][j]
            data[i][j] = min(dis1, dis2)
# print(data)

ans = 10**10
for i in permutations(r, len(r)):
    # print(i)
    ans_tmp = 0
    for j in range(len(r)-1):
        ans_tmp += data[i[j]][i[j+1]]
    ans = min(ans, ans_tmp)
print(ans)
