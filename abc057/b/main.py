#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(n)]
cd = [list(map(int, input().split())) for i in range(m)]

for a, b in ab:
    dis, index = 10**10, -1
    for i, (c, d) in enumerate(cd):
        dis_tmp = abs(a-c)+abs(b-d)
        if dis > dis_tmp:
            # print(dis)
            index = i
            dis = dis_tmp
    print(index+1)
