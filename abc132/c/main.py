#!/usr/bin/env python3

a = int(input())
d = list(map(int, input().split()))

d.sort()

center = len(d)//2-1

if d[center] == d[center+1]:
    print(0)
    exit()
else:
    d[center]

    print(d[center+1]-d[center])
    exit()
