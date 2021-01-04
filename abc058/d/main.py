#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

mod = 10**9+7

n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))


ans1 = 0
ans2 = 0
for i in range(0, n):
    ans1 += i*x[i]-(n-i-1)*x[i] % mod
    ans1 %= mod

for i in range(0, m):
    ans2 += i*y[i]-(m-i-1)*y[i] % mod
    ans2 %= mod
# print(ans1, ans2)
print(ans1*ans2 % mod)
