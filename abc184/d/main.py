#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b, c = list(map(int, input().split()))

dp = [[[0]*101 for i in range(101)] for i in range(101)]


# for x in range(101):
#     for y in range(101):
#         dp[100][y][x] = 0
# for x in range(101):
#     for z in range(101):
#         dp[z][100][x] = 0
# for y in range(101):
#     for z in range(101):
#         dp[z][y][100] = 0


for z in reversed(range(0, 100)):
    for y in reversed(range(0, 100)):
        for x in reversed(range(0, 100)):

            if x+y+z == 0:
                continue
            tmp = 0
            tmp += (dp[z+1][y][x]+1)*(z)
            tmp += (dp[z][y+1][x]+1)*(y)
            tmp += (dp[z][y][x+1]+1)*(x)
            dp[z][y][x] = tmp/(x+y+z)


print(dp[a][b][c])
