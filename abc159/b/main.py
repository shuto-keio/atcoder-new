#!/usr/bin/env python3

s = list(str(input()))
N = len(s)


def disc(s):
    s1 = s
    s2 = s[:]
    s2.reverse()
    if s1 == s2:
        return True
    else:
        return False


if disc(s) and disc(s[:(N-1)//2]) and disc(s[(N+3)//2-1:]):
    print("Yes")
else:
    print("No")
