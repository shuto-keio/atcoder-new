#!/usr/bin/env python3

x, k, d = list(map(int, input().split()))

if x < 0:
    x *= -1

num = x//d

if num >= k:
    print(x-d*k)
    exit()
else:
    tmp = k-num
    if tmp % 2 == 0:
        print(x-d*num)
    else:
        print(d*(num+1)-x)
