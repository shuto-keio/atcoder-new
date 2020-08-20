#!/usr/bin/env python3

s = str(input())

ans = 700

for i in s:
    if i == "o":
        ans += 100
print(ans)
