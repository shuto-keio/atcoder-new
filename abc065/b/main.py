#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())

a = [int(input())-1 for i in range(n)]

data = [0]*n
data[0] = 1
now = 0
count = 0
while(1):
    count += 1
    next_ = a[now]
    # print(next_)
    if data[next_] == 1:
        print(-1)
        exit()
    data[next_] = 1
    if next_ == 1:
        print(count)
        exit()
    now = next_
