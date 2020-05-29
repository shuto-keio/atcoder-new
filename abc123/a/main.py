#!/usr/bin/env python3

import itertools

abcdek = [int(input()) for _ in range(6)]


for i, j in itertools.combinations(range(5), 2):
    num1, num2 = abcdek[i], abcdek[j]
    if num2-num1 > abcdek[-1]:
        print(":(")
        exit()


print("Yay!")
