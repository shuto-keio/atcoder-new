#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = str(input())

for i in range(0, len(s)//2):
    s = s[:-2]
    # print(s)
    num = len(s)
    s1 = s[:num//2]
    s2 = s[num//2:]
    if s1 == s2:
        print(len(s))
        exit()
    # print(s1)
    # print(s2)
