#!/usr/bin/env python3
# import itertools
# import numpy as np

n, s = list(map(int, input().split()))
a = list(map(int, input().split()))

mod = 998244353

dp = [[0]*(s+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(0, n):
    for j in range(0, s+1):
        dp[i+1][j] += dp[i][j]*2 % mod

        if j+a[i] <= s:
            dp[i + 1][j + a[i]] += dp[i][j] % mod


print(dp[n][s] % mod)
