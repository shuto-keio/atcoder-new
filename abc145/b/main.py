#!/usr/bin/env python3

n = int(input())
s = list(str(input()))

if s[:len(s)//2]*2 == s:
    print("Yes")
else:
    print("No")
