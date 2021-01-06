#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

s = str(input())


count = 0
index = 0
while(index < len(s)):
    # print(index)
    if s[index] == "d":
        if s[index:index+5] == "dream":
            # print(s[index:index+8])
            if s[index+5:index+8] == "era":
                index += 5
                continue
            elif s[index+5:index+7] == "er":

                index += 7
                continue
            else:
                index += 5
                continue
    elif s[index] == "e":
        if s[index:index+6] == "eraser":
            index += 6
            continue
        elif s[index:index+5] == "erase":
            index += 5
            continue

    print("NO")
    exit()

print("YES")
