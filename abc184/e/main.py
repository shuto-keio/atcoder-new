#!/usr/bin/env python3
from collections import deque
import string
import sys
# import pprint
sys.setrecursionlimit(10**6)


h, w = list(map(int, input().split()))
a = []

data = {}
check = {}
for i in list(string.ascii_lowercase):
    data[i] = []
    check[i] = 0

for y in range(h):
    tmp = list(str(input()))
    a.append(tmp)
    for x in range(len(tmp)):
        if tmp[x] == "G":
            goal = (y, x)
        elif tmp[x] == "S":
            start = (y, x)
        elif tmp[x] == "." or tmp[x] == "#":
            continue
        else:
            data[tmp[x]].append((y, x))

# print(data)
# print(a)
map_ = [[10**10]*w for i in range(h)]
map_[start[0]][start[1]] = 0

queue = deque([start])


while queue:
    (y, x) = queue.popleft()
    now = map_[y][x]

    if a[y][x] == "G":
        print(now)
        exit()
    if a[y][x] != "." and a[y][x] != "#" and a[y][x] != "S":
        if check[a[y][x]] == 0:
            check[a[y][x]] = 1
            for y_tmp, x_tmp in data[a[y][x]]:
                if map_[y_tmp][x_tmp] > now+1:
                    map_[y_tmp][x_tmp] = now+1
                    queue.append((y_tmp, x_tmp))

    for y_tmp, x_tmp in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
        if x_tmp >= 0 and x_tmp < w and y_tmp >= 0 and y_tmp < h:

            if a[y_tmp][x_tmp] != "#":
                if map_[y_tmp][x_tmp] > now+1:
                    map_[y_tmp][x_tmp] = now+1
                    queue.append((y_tmp, x_tmp))


# pprint.pprint(map_)


print(-1)
