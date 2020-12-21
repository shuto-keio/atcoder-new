#!/usr/bin/env python3
import sys
import math
sys.setrecursionlimit(10**6)

n, a, b = list(map(int, input().split()))
h = [int(input()) for i in range(n)]

# print(h)


def judge(num):
    diff = a-b
    count = 0
    for i in range(len(h)):
        tmp = max(0, h[i]-num*b)
        count += math.ceil(tmp/diff)
        if count > num:
            return False
        # print(h[i], num*b, num)
    return True


min_, max_ = 0, 10**9

while(1):
    index = (min_+max_)//2
    result = judge(index)
    if result:
        max_ = index
    else:
        min_ = index

    # print(min_, max_)

    if (max_-min_) <= 1:
        break

if judge(min_):
    print(min_)
else:
    print(max_)
