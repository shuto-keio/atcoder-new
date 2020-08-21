#!/usr/bin/env python3

import bisect

n = int(input())
a = list(map(int, input().split()))

a.sort()

if n == 2:
    print(a[1], a[0])
    exit()
# value = comb(a[1], a[0], exact=True)
# ans = [a[1], a[0]]
# index = 0
# for i in range(2, n):
#     value_tmp = comb(a[i], a[index], exact=True)
#     x = a[i]
#     y = a[index]
#     diff = abs((x-2*y)//2)
#     while 1:
#         y_new = a[index+1]
#         diff_new = abs((x-2*y_new)//2)
#         if diff_new > diff:
#             break
#         else:
#             index += 1
#     if value_tmp > value:
#         ans = [a[i], a[index]]
#         # value = value_tmp
# print(*ans)

x = a[-1]
index = bisect.bisect_left(a[:n-1], x/2)

ans = []
ans.append([abs(x/2-a[index-1]), a[index-1]])
ans.append([abs(x/2-a[index]), a[index]])
# ans.append([abs(x/2-a[index+1]), a[index+1]])

ans.sort()

print(x, ans[0][1])
