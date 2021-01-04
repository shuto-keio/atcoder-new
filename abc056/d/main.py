#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()


def solve(index):
    a_tmp = a[:]
    del a_tmp[index]

    dp = [[0]*(k+1) for i in range(len(a_tmp)+1)]
    # for i in range(len(a_tmp)+1):
    #     for j in range(k+1):
    #         dp[i][0] = 1
    #         dp[0][j] = 1
    dp[0][0] = 1

    for i in range(0, len(a_tmp)):
        for j in range(0, k):
            num = a_tmp[i]
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j+num < (k+1):
                dp[i+1][j+num] = max(dp[i][j], dp[i+1][j+num])
    ans_tmp = 1
    for i in range(max(0, k-a[index]), k):
        # print(i)
        if dp[-1][i] == 1:
            ans_tmp = 0
            break
    # if ans_tmp == 0:
    #     ans_list[index] = 1

    return ans_tmp == 0


# print(a)
ans_list = [-1]*n
# ans = 0
index_min = 0
index_max = n
while(abs(index_max-index_min) >= 2):
    index = (index_max+index_min)//2
# def solve(index):
    a_tmp = a[:]
    del a_tmp[index]

    dp = [[0]*(k+1) for i in range(len(a_tmp)+1)]
    # for i in range(len(a_tmp)+1):
    #     for j in range(k+1):
    #         dp[i][0] = 1
    #         dp[0][j] = 1
    dp[0][0] = 1

    for i in range(0, len(a_tmp)):
        for j in range(0, k):
            num = a_tmp[i]
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j+num < (k+1):
                dp[i+1][j+num] = max(dp[i][j], dp[i+1][j+num])
    ans_tmp = 1
    for i in range(max(0, k-a[index]), k):
        # print(i)
        if dp[-1][i] == 1:
            ans_tmp = 0
            break
    # if ans_tmp == 0:
    #     ans_list[index] = 1

    # return ans_tmp == 0
    res = ans_tmp == 0
    if res:
        ans_list[index] = 1
        index_max = index
    else:
        ans_list[index] = 0
        index_min = index
    # print(ans_list)
    # print(index_min, index_max)

if index_min >= 0:
    ans_list[index_min] = int(solve(index_min))
if index_max < n:
    ans_list[index_max] = int(solve(index_max))

# print(ans_list)
ans = n
for i in range(len(ans_list)):
    if ans_list[i] == 1:
        ans = i
        break
print(ans)
