#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)


s1 = list(str(input()))
s2 = list(str(input()))

if len(s2) == len(s1):
    for i in range(len(s2)):
        print("{}{}".format(s1[i], s2[i]), end="")
    print()
else:
    for i in range(len(s2)):
        print("{}{}".format(s1[i], s2[i]), end="")

    print(s1[-1])
