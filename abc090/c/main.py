#!/usr/bin/env python3

n, m = list(map(int, input().split()))


if n == 1 and m == 1:
    corner = 1
    edge = 0
    other = 0
    print(1)
elif n == 1 or m == 1:
    corner = 2
    edge = n*m-corner
    other = 0
    print(edge)
else:
    corner = 4
    edge = n*2+m*2-corner*2
    other = n*m - edge-corner
    print(other)
