#!/usr/bin/env python3

n = int(input())
s, t = list(map(str, input().split()))


for i in range(n):
    print(s[i], end="")
    print(t[i], end="")
