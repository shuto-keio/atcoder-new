#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = set(list(str(input())))

all_ = [chr(i) for i in range(97, 97+26)]

for i in all_:
    if i in s:
        continue
    else:
        print(i)
        exit()
print("None")
