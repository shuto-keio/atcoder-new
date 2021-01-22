#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

sa = list(str(input()))
sb = list(str(input()))
sc = list(str(input()))

index_a = -1
index_b = -1
index_c = -1
turn = "a"
while(1):
    if turn == "a":
        index_a += 1
        if len(sa) == index_a:
            print("A")
            break
        turn = sa[index_a]
    elif turn == "b":
        index_b += 1
        if len(sb) == index_b:
            print("B")
            break
        turn = sb[index_b]
    elif turn == "c":
        index_c += 1
        if len(sc) == index_c:
            print("C")
            break
        turn = sc[index_c]
