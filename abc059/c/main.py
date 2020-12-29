#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

ans1 = 0
sum1 = 0
for i in range(len(a)):
    sum1 += a[i]
    if i % 2 == 0:
        if sum1 > 0:
            continue
        else:
            ans1 += -sum1 + 1
            sum1 = 1
    elif i % 2 == 1:
        if sum1 < 0:
            continue
        else:
            ans1 += sum1 + 1
            sum1 = -1


ans2 = 0
sum2 = 0
for i in range(len(a)):
    sum2 += a[i]
    if i % 2 == 1:
        if sum2 > 0:
            continue
        else:
            ans2 += -sum2 + 1
            sum2 = 1
    elif i % 2 == 0:
        if sum2 < 0:
            continue
        else:
            ans2 += sum2 + 1
            sum2 = -1

print(min(ans1, ans2))
