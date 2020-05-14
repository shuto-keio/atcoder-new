#!/usr/bin/env python3
import math

a, b, x = list(map(int, input().split()))


def calc(x):

    return a*x+b*int(len(str(x)))


min_value = (1, calc(1))
max_value = (10**9, calc(10**9))
# print(min_value)
# print(max_value)
# print(x, calc(x))

if x < min_value[1]:
    print(0)
    exit()
elif x >= max_value[1]:
    print(max_value[0])
    exit()

while(1):
    mid = (min_value[0]+max_value[0])//2
    mid_value = (mid, calc(mid))
    # print(min_value, mid_value, max_value)

    if max_value[0] - min_value[0] <= 1:
        if max_value[1] == x:
            print(max_value[0])
        else:
            print(min_value[0])
        exit()

    if x < mid_value[1]:
        max_value = mid_value
    elif x > mid_value[1]:
        min_value = mid_value
    else:
        print(mid_value[0])
        exit()
