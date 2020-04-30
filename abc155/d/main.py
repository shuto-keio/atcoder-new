#!/usr/bin/env python3

import numpy as np:

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = np.array(a)

minus = np.sum(a > 0)
zero = np.sum(a == 0)
plus = np.sum(a > 0)

num_minus = minus * plus
num_zero = zero * (minus + plus)
num_plus = (plus * (plus-1) + minus * (minus-1))//2

if k <= num_minus:

elif k <= (num_minus+num_zero):

else:
