#!/usr/bin/env python3

h, w = list(map(int, input().split()))

ss = [list(str(input())) for _ in range(h)]

dp = [[100*100 for _ in range(w)] for i in range(h)]  # dp[h][w]

if ss[0][0] == "#":
    dp[0][0] = 1
else:
    dp[0][0] = 0
# print(dp)

for h_tmp in range(0, h):
    for w_tmp in range(0, w):
        if w_tmp > 0:
            # print(dp[h_tmp][w_tmp-1])
            if ss[h_tmp][w_tmp-1] == "." and ss[h_tmp][w_tmp] == "#":
                dp[h_tmp][w_tmp] = min(dp[h_tmp][w_tmp], dp[h_tmp][w_tmp-1]+1)
            else:
                dp[h_tmp][w_tmp] = min(dp[h_tmp][w_tmp], dp[h_tmp][w_tmp-1])
        if h_tmp > 0:
            # print(dp[h_tmp][w_tmp-1])
            if ss[h_tmp-1][w_tmp] == "." and ss[h_tmp][w_tmp] == "#":
                dp[h_tmp][w_tmp] = min(dp[h_tmp][w_tmp], dp[h_tmp-1][w_tmp]+1)
            else:
                dp[h_tmp][w_tmp] = min(dp[h_tmp][w_tmp], dp[h_tmp-1][w_tmp])

# print(dp)
print(dp[-1][-1])
