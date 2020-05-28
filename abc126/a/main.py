#!/usr/bin/env python3

n, k = list(map(int, input().split()))
s = list(str(input()))

s[k-1] = chr(ord(s[k-1])+32)

print("".join(s))
