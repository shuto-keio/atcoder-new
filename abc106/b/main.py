#!/usr/bin/env python3

n = int(input())


ans = 0
for i in range(1, n+1):
    if i % 2 == 0:
        continue
    tmp = 0
    for j in range(1, i+1):
        if i % j == 0:
            tmp += 1
    if tmp == 8:
        ans += 1

print(ans)
