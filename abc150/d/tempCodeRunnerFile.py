#!/usr/bin/env python3

import fractions
import numpy as np
import math

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a = list(set(a))

a = np.array(a)//2

gcd_a = a[0]
for i in range(1, len(a)):
    gcd_a = fractions.gcd(gcd_a, a[i])

lcd_a = a[0]
for i in range(1, len(a)):
    lcd_a = lcd_a * a[i] // fractions.gcd(lcd_a, a[i])


a_ = a//gcd_a
a_ = (a_+1) % 2

if np.any(a_) is True:
    print(0)
else:
    print(math.ceil(m//(lcd_a)/2))
