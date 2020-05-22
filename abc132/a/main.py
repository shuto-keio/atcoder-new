#!/usr/bin/env python3

s = list(str(input()))

if len(set(s)) != 2:
    print("No")
    exit()

for i in list(set(s)):
    if s.count(i) != 2:
        print("No")
        exit()

print("Yes")
