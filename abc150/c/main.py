#!/usr/bin/env python3
import math

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

ans = 0


def calc(data):
    ans = 0
    flag = [1]*n
    for i in range(len(data)):
        num = data[i]
        sum_ = sum(flag[:max(0, num-1)])
        ans += sum_*math.factorial(len(data)-i-1)
        flag[num-1] = 0
    return ans


ans = calc(p)-calc(q)

print(abs(ans))
