#!/usr/bin/env python3

s = list(str(input()))

s.reverse()
# print(s)
mod = 10**9+7

dp = [[0]*13 for _ in range(len(s)+1)]
dp[0][0] = 1
# if s[0] == "?":
#     dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
# else:
#     num = int(s[0]) % 13
#     dp[1][num] += 1
# print(s[0])
# print(dp)
p = 1
for i in range(0, len(s)):
    # print(s[i])
    if s[i] == "?":
        for j in range(10):
            num = j*p
            num %= 13
            for j in range(13):
                dp[i+1][(j+num) % 13] += dp[i][j] % mod
    else:
        num = (int(s[i]) * p) % 13
        for j in range(13):
            dp[i+1][(j+num) % 13] += dp[i][j]
    # print(dp)
    p *= 10
print(dp[-1][5] % mod)
