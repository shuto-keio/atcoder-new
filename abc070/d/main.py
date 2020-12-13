#!/usr/bin/env python3
from collections import deque
import sys
sys.setrecursionlimit(10**6)


n = int(input())
abc = [list(map(int, input().split())) for i in range(n-1)]
q, k = list(map(int, input().split()))
xy = [list(map(int, input().split())) for i in range(q)]

dis_data = {}
for i in range(n):
    dis_data[i] = {}

for i in range(len(abc)):
    a, b, c = abc[i]
    dis_data[a-1][b-1] = c
    dis_data[b-1][a-1] = c
# print(dis_data)

data = [-1]*n

q = deque([(k-1, 0)])

while(q):
    index, dis = q.pop()
    data[index] = dis

    route_dict = dis_data[index]
    for key, value in route_dict.items():
        if data[key] == -1:
            data[key] = dis+value
            q.append((key, dis+value))

# print(data)

for x, y in xy:
    x -= 1
    y -= 1

    print(data[x]+data[y])
