#!/usr/bin/env python3

n = int(input())

ans = 0
for i in range(1, n+1):
    num = n//i
    ans += (1+num)*i*num//2

print(ans)
