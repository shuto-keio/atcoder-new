#!/usr/bin/env python3

n = int(input())
w = list(map(int, input().split()))

sum_w = sum(w)

ans = sum_w
value = 0

for i in range(0, n):
    value += w[i]
    ans_tmp = abs((sum_w-value)-value)
    ans = min(ans, ans_tmp)
print(ans)
