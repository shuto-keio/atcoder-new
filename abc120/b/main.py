#!/usr/bin/env python3

a, b, k = list(map(int, input().split()))

ans = []

for i in range(1, 101):
    if a % i == 0 and b % i == 0:
        ans.append(i)
# print(ans)
ans.reverse()
print(ans[k-1])
