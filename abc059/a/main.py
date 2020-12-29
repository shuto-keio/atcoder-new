#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = [chr(ord(i[0])-32) for i in list(map(str, input().split()))]

print("".join(s))
