#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

data = [0] * 8
ans = 0
strong = 0
for i in a:
    quo = i // 400
    if quo >= 8:
        strong += 1
    else:
        data[quo] += 1

for i in data:
    if i >= 1:
        ans += 1

print(max(1, ans), ans+strong)
