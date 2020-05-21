#!/usr/bin/env python3

h, w, a, b = list(map(int, input().split()))

for h_tmp in range(h):
    for w_tmp in range(w):
        if (w_tmp < a and h_tmp < b) or (w_tmp >= a and h_tmp >= b):
            print(0, end="")
        else:
            print(1, end="")
    print()
