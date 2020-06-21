#!/usr/bin/env python3

s = str(input())


ans = 999
for i in range(len(s)-2):
    num = int(s[i:i+3])
    ans = min(ans, abs(num-753))
print(ans)
