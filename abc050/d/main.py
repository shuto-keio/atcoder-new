#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)


for a in range(1, 10):
    for v in range(1, 10):

        print(a ^ (v-a), a)
