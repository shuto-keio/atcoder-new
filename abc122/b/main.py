#!/usr/bin/env python3

s = list(str(input()))

set_ = set(["A", "C", "G", "T"])

ans = 0
count = 0
for i in range(len(s)):
    if s[i] in set_:
        count += 1
    else:
        ans = max(ans, count)
        count = 0

ans = max(ans, count)

print(ans)
