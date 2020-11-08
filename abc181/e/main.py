#!/usr/bin/env python3
import bisect
from itertools import accumulate
import sys
sys.setrecursionlimit(10**6)


n, m = list(map(int, input().split()))
h = list(map(int, input().split()))
w = list(map(int, input().split()))

h.sort()
w.sort()

# print(h)
# print(w)


data_h = [0]
for i in range(0, (n)//2):
    data_h.append(h[2*i+1]-h[2*i])

data_h_rev = [0]
for i in range(0, (n)//2):
    data_h_rev.append(h[2*i+1+1]-h[2*i+1])

ac_data_h = list(accumulate(data_h))
ac_data_h_rev = list(accumulate(data_h_rev))

ans = 10**10
# index = 0
# for i in range(len(h)//2+1):
#     # print(w[index])
#     if h[i*2] > w[index]:
#         for index_tmp in range(index, len(w)-1):
#             if abs(w[index_tmp]-h[i*2]) > abs(w[index_tmp+1]-h[i*2]):
#                 index = index_tmp+1
#             else:
#                 break

#     # num1 = w[index]
#     ans_tmp = 0
#     ans_tmp += ac_data_h[i]
#     ans_tmp += ac_data_h_rev[-1]-ac_data_h_rev[i]
#     ans_tmp += abs(h[i*2]-w[index])

#     print(h[i*2], w[index], ans_tmp)
#     ans = min(ans, ans_tmp)

for num in w:
    x = bisect.bisect(h, num)
    i = x//2

    ans_tmp = 0
    ans_tmp += ac_data_h[i]
    ans_tmp += ac_data_h_rev[-1]-ac_data_h_rev[i]
    ans_tmp += abs(h[i*2]-num)

    ans = min(ans, ans_tmp)

print(ans)
