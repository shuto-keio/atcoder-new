#!/usr/bin/env python3

s = int(input())

a = set([s])


for i in range(2, 1000001):
    # print(s)
    if s % 2 == 0:
        s = s//2
    else:
        s = 3*s+1
    if s in a:
        print(i)
        exit()
    a.add(s)
