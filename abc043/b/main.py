#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = list(str(input()))

ans = []
for i in s:
    if i == "B":
        if len(ans) >= 1:
            ans.pop()
        else:
            pass
    else:
        ans.append(i)

print("".join(ans))
