#!/usr/bin/env python3

s = list(str(input()))


for i in range(len(s)):
    if (i+1) % 2 == 1:
        if s[i] not in ["R", "U", "D"]:
            print("No")
            exit()
    elif (i+1) % 2 == 0:
        if s[i] not in ["L", "U", "D"]:
            print("No")
            exit()
print("Yes")
