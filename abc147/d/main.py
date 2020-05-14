#!/usr/bin/env python3

# mod = 10**9+7

# n = int(input())
# a = list(map(int, input().split()))

# max_digit = 61

# count_0 = [0 for _ in range(max_digit)]
# count_1 = [0 for _ in range(max_digit)]

# for i in range(len(a)):
#     num_str = bin(a[i])[2:]
#     # print(num_str)
#     for j in range(len(num_str)):
#         # print(num_str[-j-1])
#         if num_str[-j-1] == "1":
#             count_1[-j-1] += 1

# # for i in range(max_digit):
# #     count_0[i] = n-count_1[i]

# ans = 0
# count = 1
# for i in range(61):
#     # tmp = count_0[-i-1]*count_1[-i-1]
#     tmp = count_1[-i-1]*(n-count_1[-i-1])
#     ans += tmp*count
#     count = (count*2) % mod
# print(ans % mod)


n = int(input())
a = list(map(int, input().split()))

mod = 10**9+7
max_digit = 61

ans = 0
m = 1
for _ in range(max_digit):
    bit = sum(x & m for x in a)
    bit //= m
    non_bit = n - bit
    ans = (ans+bit*non_bit*m) % mod
    m <<= 1
print(ans)
