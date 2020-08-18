#!/usr/bin/env python3

n = int(input())
s = list(str(input()))

ans = 0
for i in range(1, n):
    a, b = set(s[:i]), set(s[i:])
    ans_tmp = len(a & b)
    ans = max(ans, ans_tmp)
print(ans)
