#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

h, w = list(map(int, input().split()))

print("#"*(w+2))
for i in range(h):
    a = str(input())
    print("#{}#".format(a))
print("#"*(w+2))
