#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())

data = [[0]*26 for i in range(n)]
for i in range(n):
    s = list(str(input()))

    for j in s:
        data[i][ord(j)-97] += 1


ans = [10**10]*26
for i in data:
    for j in range(26):
        ans[j] = min(ans[j], i[j])

for i in range(len(ans)):
    tmp = chr(i+97)
    print(tmp*ans[i], end="")
print()
