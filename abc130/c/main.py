#!/usr/bin/env python3

w, h, x, y = list(map(int, input().split()))

if w/2 == x and h/2 == y:
    print(w*h/2, 1)
else:
    print(w*h/2, 0)
