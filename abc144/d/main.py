#!/usr/bin/env python3
import math

a, b, x = list(map(int, input().split()))

if 2*x >= a*a*b:
    tan_theta = 2*(b*a*a-x)/(a*a*a)
else:
    tan_theta = a*b*b/(2*x)

print(math.atan(tan_theta)/math.pi*180)
