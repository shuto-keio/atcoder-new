#!/usr/bin/env python3
# import numpy as np
# from collections import deque
import sys
sys.setrecursionlimit(10**6)


# def tansaku(x, y):
#     dis_base = a[x][y]
#     dis_lists = [10**10]*n
#     dis_lists[x] = 0

#     goal = y
#     now = x
#     dis = 0

#     d = deque([(now, dis)])

#     while(d):
#         # break
#         now, dis = d.pop()
#         if now == goal:
#             dis_lists[now] = min(dis, dis_lists[now])
#             continue

#         for i in map_set[now]:
#             dis_tmp = a[now][i]+dis
#             if dis_lists[i] > dis_tmp:
#                 dis_lists[i] = dis_tmp
#                 d.append((i, dis_tmp))

#     if dis_lists[y] > dis_base:
#         return 1
#     elif dis_lists[y] == dis_base:
#         return 0
#     else:
#         print(-1)
#         exit()


# n = int(input())
# a = [list(map(int, input().split())) for i in range(n)]


# if n == 1:
#     print(a[0])
#     exit()
# if n == 2:
#     print(a[0][-1])
#     exit()

# dis_list = []
# for y in range(n):
#     for x in range(n):
#         if x > y:
#             dis_list.append([(y, x), a[y][x]])

# dis_list = sorted(dis_list, key=lambda x: x[1])

# # print(dis_list)
# min_dis = dis_list[0][1]+dis_list[1][1]

# # map_ = np.zeros((n, n), dtype=np.int64)
# map_ = [[0]*n for i in range(n)]
# map_set = [[] for i in range(n)]

# (y, x), dis = dis_list[0]
# map_[y][x] = 1
# # map_[x][y] = 1
# map_set[x].append(y)
# map_set[y].append(x)


# (y, x), dis = dis_list[1]
# map_[y][x] = 1
# # map_[x][y] = 1
# map_set[x].append(y)
# map_set[y].append(x)

# # print(map_)
# for i in range(2, len(dis_list)):
#     (y, x), dis = dis_list[i]
#     if dis < min_dis:
#         map_[y][x] = 1
#         # map_[x][y] = 1
#         map_set[x].append(y)
#         map_set[y].append(x)
#         continue

#     flag = tansaku(x, y)

#     # print(x, y, flag)
#     if flag == 1:
#         map_[y][x] = 1
#         # map_[x][y] = 1
#         map_set[x].append(y)
#         map_set[y].append(x)

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

map_ = [[True]*n for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):

            # tmp = [0]*n

            if a[i][j] > a[i][k] + a[k][j]:
                print(-1)
                exit()
            if a[i][j] == a[i][k]+a[k][j]:
                if i == k or i == j or k == j:
                    continue
                # if a[i][j] == a[i][k]+a[k][j]:
                map_[i][j] = False

# print(map_)
ans = 0
for y in range(n):
    for x in range(y+1, n):
        if map_[y][x] == 1:
            ans += a[y][x]
print(ans)
