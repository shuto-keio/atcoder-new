#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, k = list(map(int, input().split()))
l_ = list(map(int, input().split()))

l_.sort(reverse=True)

print(sum(l_[:k]))
