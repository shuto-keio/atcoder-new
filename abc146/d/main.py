#!/usr/bin/env python3

from collections import deque

n = int(input())

connect_list = [[] for _ in range(n)]

ab = [list(map(int, input().split())) for i in range(n-1)]

for i in range(n-1):
    a, b = ab[i]
    connect_list[a-1].append(b-1)
    connect_list[b-1].append(a-1)


color_list = {}
check_list = [0]*n

color_max = max(map(len, connect_list))

vertex = [0 for i in range(n)]
d = deque([0])

while(len(d) > 0):
    # print(d)
    index = d.pop()
    check_list[index] = 1

    index_list = connect_list[index]

    for i in index_list:
        if check_list[i] == 1:
            continue

        check_list[i] = 1
        d.append(i)
        num = vertex[index] % color_max+1
        color_list[(min(index, i), max(index, i))] = num
        vertex[index], vertex[i] = num, num

print(color_max)
for a, b in ab:
    print(color_list[(a-1, b-1)])
