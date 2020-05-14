#!/usr/bin/env python3

import itertools

n = int(input())

xy = []
for i in range(n):
    a = int(input())
    xy.append([list(map(int, input().split())) for _ in range(a)])
ans = 0
for i in itertools.product([0, 1], repeat=n):
    honest_list = list(i)
    flag = 0
    for index in range(n):
        if i[index] == 0:
            continue
        xy_tmp = xy[index]
        # print(xy_tmp)
        for k in range(len(xy_tmp)):
            x, y = xy_tmp[k]

            if honest_list[x-1] != y:
                flag = 1
            # if honest_list[x-1] == -1:
            #     honest_list[x-1] = y
            # else:  # 0or1
            #     if honest_list[x-1] != y:
            #         flag = 1
            #         break
            #     else:
            #         continue

        # if flag == 1:
        #     break
    if flag != 1:
        ans = max(ans, sum(honest_list))

print(ans)
