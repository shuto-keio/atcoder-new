#!/usr/bin/env python3

s = str(input())

if s == "RRR":
    print(3)
elif s[0:2] == "RR" or s[1:3] == "RR":
    print(2)
elif "R" in set(list(s)):
    print(1)
else:
    print(0)
