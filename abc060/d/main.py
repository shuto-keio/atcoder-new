#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, W = list(map(int, input().split()))
w, v = [], []
for i in range(n):
    w_, v_ = list(map(int, input().split()))
    w.append(w_)
    v.append(v_)

sum_w = 0
for i in range(len(w)):
    sum_w += w[i]-w[0]
# print(sum_w)

dp = [[[0]*(sum_w+1) for i in range(n+1)] for i in range(n+1)]

for i in range(0, n):
    w_, v_ = w[i], v[i]
    w_ -= w[0]
    for j in range(0, n):
        for k in range(0, max(1, sum_w)):
            # print(i, j, k)
            dp[i+1][j][k] = max(dp[i][j][k], dp[i+1][j][k])
            if k+w_ < sum_w+1:
                dp[i+1][j+1][k+w_] = max(dp[i][j][k]+v_, dp[i+1][j+1][k+w_])
ans = 0
for i in range(0, n+1):
    for j in range(0, n+1):
        for k in range(0, sum_w+1):
            weight = k+w[0]*j
            if weight <= W:
                # print(i, j, k, dp[i][j][k])
                ans = max(ans, dp[i][j][k])

# print(dp)
print(ans)
