#!/usr/bin/env python3
import bisect
import copy
import sys
sys.setrecursionlimit(10**6)


n, t = list(map(int, input().split()))
a = list(map(int, input().split()))

x = a[:n//2]
y = a[n//2:]

data_x = [0]
for i in x:
    tmp = copy.copy(data_x)
    for j in data_x:
        if i+j <= t:
            tmp.append(i+j)
    data_x = tmp


data_y = [0]
for i in y:
    tmp = copy.copy(data_y)
    for j in data_y:
        if i+j <= t:
            tmp.append(i+j)
    data_y = tmp

data_x.sort()
data_y.sort()

# print(data_x)
# print(data_y)

ans = 10**10

for i in data_x:
    rem = t-i

    index = bisect.bisect_right(data_y, rem)
    if index-1 >= 0 and index-1 < len(data_y):
        ans_tmp = t-(i + data_y[index-1])
        ans = min(ans, ans_tmp)
    # if index >= 0 and index < len(data_y):
    #     ans_tmp = t-(i + data_y[index])
    #     ans = min(ans, ans_tmp)
    # if index+1 >= 0 and index+1 < len(data_y):
    #     ans_tmp = t-(i + data_y[index+1])
    #     ans = min(ans, ans_tmp)

print(t-ans)
