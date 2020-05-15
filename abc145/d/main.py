#!/usr/bin/env python3

mod = 10**9+7

x, y = list(map(int, input().split()))

# dp = [[0]*(y+1) for _ in range(x+1)]
# dp[0][0] = 1
# for x_tmp in range(1, x+1):
#     for y_tmp in range(1, y+1):
#         print(x_tmp, y_tmp)

#         if x_tmp-2 >= 0 and y_tmp-1 >= 0:
#             dp[x_tmp][y_tmp] += dp[x_tmp-2][y_tmp-1] % mod
#         if x_tmp-1 >= 0 and y_tmp-2 >= 0:
#             dp[x_tmp][y_tmp] += dp[x_tmp-1][y_tmp-2] % mod

# print(dp[-1][-1] % mod)


def comb(n, r):
    X = Y = 1
    if r < 0 or n < r:
        return 0
    if r == 0:
        return 1
    if n-r < r:
        r = n-r
    for i in range(1, r+1):
        Y = Y*i % mod
        X = X*(n-i+1) % mod
    Y = pow(Y, mod-2, mod)
    return X*Y


if (x+y) % 3 != 0:
    print(0)
    exit()

num = min(x, y)-(x+y)//3
if num < 0:
    print(0)
    exit()

# print((x+y)//3, num)
print(comb((x+y)//3, num) % mod)
