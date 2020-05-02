#!/usr/bin/env python3

# import fractions
# import numpy as np
# import math

# n, m = list(map(int, input().split()))
# a = list(map(int, input().split()))
# a = list(set(a))

# a = np.array(a)//2

# gcd_a = a[0]
# for i in range(1, len(a)):
#     gcd_a = fractions.gcd(gcd_a, a[i])

# lcd_a = a[0]
# for i in range(1, len(a)):
#     lcd_a = lcd_a * a[i] // fractions.gcd(lcd_a, a[i])


# a_ = a//gcd_a
# a_ = a_ % 2
# if np.any(a_ == 0) is True:
#     print(0)
# else:
#     print(math.ceil(m//(lcd_a)/2))


from fractions import gcd
n, m = map(int, input().split())
a = [int(i)//2 for i in input().split()]


def lcm(x, y):
    return x*y//gcd(x, y)


l = 1
for i in a:
    l = lcm(l, i)
for i in a:
    if l//i % 2 == 0:
        print(0)
        exit()
print((m//l+1)//2)
