#!/usr/bin/env python3

n = int(input())
s = list(str(input()))


base_a = ord("A")

for i in range(len(s)):
    index = (ord(s[i])-base_a+n) % 26 + base_a
    s[i] = chr(index)

for i in range(len(s)):
    print(s[i], end="")
print()
