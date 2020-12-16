#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

abc = list(map(int, input().split()))
abc.sort()

print(sum(abc[:2]))
