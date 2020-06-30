#!/usr/bin/env python3

s = list(str(input()))
t = list(str(input()))

ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans += 1
print(ans)
