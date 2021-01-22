#!/usr/bin/env python3
import itertools
import sys
sys.setrecursionlimit(10**6)

s = str(input())

ans = 0
for rp in range(1, len(s)):
    for i in itertools.combinations(range(1, len(s)), rp):
        # print(i)
        # tmp = ""
        index = 0
        for j in i:
            tmp = int(s[index:j])
            ans += tmp
            # print(tmp)
            index = j

        tmp = int(s[index:])
        ans += tmp
        # print(tmp)

print(ans+int(s))
