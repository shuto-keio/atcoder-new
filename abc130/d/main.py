#!/usr/bin/env python3

# from collections import deque

# n, k = list(map(int, input().split()))
# a = list(map(int, input().split()))


# def judge(a):
#     a = [i >= k for i in a]
#     return sum(a)


# def make_next_list(a, b):
#     new_a = [a[i]+a[i+1]-b[i]for i in range(len(a)-1)]
#     new_b = a[1:]
#     return new_a, new_b

# n, k = list(map(int, input().split()))
# a = list(map(int, input().split()))

# data = {}
# # data[(0, n)] = sum(a)

# d = deque([(0, n)])
# ans = 0
# while(len(d) > 0):
#     start, end = d.pop()
#     # print(start, end)
#     # print(a[start:end])
#     if start < 0 or end > n:
#         continue
#     if (start, end) in data:
#         continue
#     if (start, end+1) in data:
#         sum_ = data[(start, end+1)]-a[end]
#     else:
#         sum_ = sum(a[start:end])
#     data[(start, end)] = sum_
#     # print(sum_)
#     if sum_ >= k:
#         ans += 1
#         d.extendleft([(start, end-1), (start+1, end)])

# print(ans)

# n, k = list(map(int, input().split()))
# a = list(map(int, input().split()))

# ans = 0
# for left in range(n):
#     index = left
#     num = 0
#     while(index < n):
#         num += a[index]
#         if num >= k:
#             break
#         index += 1
#     ans += n-index
# print(ans)

import bisect
import itertools

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
s = [0] + list(itertools.accumulate(a))

ans = 0
for i in range(n):
    ans += n + 1 - bisect.bisect_left(s, k+s[i])

print(ans)
