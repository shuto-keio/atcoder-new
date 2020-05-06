#!/usr/bin/env python3

import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


x = int(input())

if x == 2:
    print(2)
    exit()
if x % 2 == 0:
    x += 1

while 1:
    if is_prime(x):
        print(x)
        exit()
    else:
        x += 2
