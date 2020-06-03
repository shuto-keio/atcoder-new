#!/usr/bin/env python3

n = int(input())

bit = 380000

ans = 0
for i in range(n):
    value, type_ = list(map(str, input().split()))
    value = float(value)
    if type_ == "JPY":
        ans += value
    else:
        ans += bit*value
print(ans)
