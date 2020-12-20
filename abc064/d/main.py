#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
s = str(input())


l_from_l = [0]*(n+1)
r_from_l = [0]*(n+1)
for i in range(0, len(s)):
    l_from_l[i+1] = l_from_l[i]
    r_from_l[i+1] = r_from_l[i]

    if s[i] == "(":
        l_from_l[i+1] += 1
    else:
        r_from_l[i+1] += 1

l_from_r = [0]*(n+1)
r_from_r = [0]*(n+1)
num = 0
for i in range(0, len(s)):
    l_from_r[-i-2] = l_from_r[-i-1]
    r_from_r[-i-2] = r_from_r[-i-1]

    if s[-i-1] == "(":
        l_from_r[-i-2] += 1
    else:
        r_from_r[-i-2] += 1


max_l = 0
max_r = 0
for i in range(n+1):
    max_l = max(max_l, -l_from_l[i]+r_from_l[i])
    max_r = max(max_r, l_from_r[i]-r_from_r[i])

# print(max_l)
# print(max_r)

ans = "("*max_l + s + ")"*max_r

print(ans)
