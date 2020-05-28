#!/usr/bin/env python3

s = str(input())

a = s[0:2]

b = s[2:]


def div(a):
    a = int(a)
    if a <= 12 and a >= 1:
        return "BOTH"
    else:
        return "YY"


if div(a) == div(b):
    if div(a) == "YY":
        print("NA")
    else:
        print("AMBIGUOUS")
elif div(a) == "YY":
    print("YYMM")
else:
    print("MMYY")
