#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)


s = list(str(input()))

ans = 0
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == "g":
            pass
        else:
            ans -= 1
    else:
        if s[i] == "g":
            ans += 1
        else:
            pass

print(ans)
