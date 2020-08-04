#!/usr/bin/env python3

s = str(input())
t = str(input())


for i in range(len(s)):
    if s[-i-1:]+s[:-i-1] == t:
        print("Yes")
        exit()

print("No")
