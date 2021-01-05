#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

max_ma, max_mb = 500, 500

n, ma, mb = list(map(int, input().split()))
abc = [list(map(int, input().split())) for i in range(n)]

dp = [[[10**10]*(max_ma+1) for i in range(max_mb+1)] for i in range(n+1)]

dp[0][0][0] = 0
for i in range(n):
    a, b, c = abc[i]
    # print(a, b, c)
    for j in range(max_ma+1):
        for k in range(max_mb+1):
            dp[i+1][k][j] = min(dp[i][k][j], dp[i+1][k][j])
            if j+a <= max_ma and k+b <= max_mb:
                # print(dp[i+1][j+a][k+b])
                dp[i+1][k+b][j+a] = min(dp[i+1][k+b][j+a], dp[i][k][j]+c)
            # exit()
    # print(dp[i+1])

# print(dp[-1][3][3])

ans = 10**10
count = 1
while(1):
    ma_tmp, mb_tmp = ma*count, mb*count
    if ma_tmp <= max_ma and mb_tmp <= max_mb:
        ans = min(dp[-1][mb_tmp][ma_tmp], ans)
    else:
        break
    # print(mb_tmp, ma_tmp)
    count += 1

if ans == 10**10:
    print(-1)
else:
    print(ans)
