#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

c = str(input())

if c in ["a", "e", "i", "o", "u"]:
    print("vowel")
else:
    print("consonant")
