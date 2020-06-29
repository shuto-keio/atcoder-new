#!/usr/bin/env python3

n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]


for x in range(0, 101):
    for y in range(0, 101):
        H_less = 10**10
        H = -1
        flag = 0
        for x_, y_, h_ in xyh:
            if h_ == 0:
                H_less = min(abs(x_-x)+abs(y_-y), H_less)
            else:
                h_tmp = h_ + abs(x_-x) + abs(y_-y)
                if H != -1:
                    if H != h_tmp:
                        flag = 1
                        break
                H = h_tmp
        if flag == 1:
            continue
        # print(H, H_less)
        if H > H_less:
            continue
        print(x, y, H)
        exit()
