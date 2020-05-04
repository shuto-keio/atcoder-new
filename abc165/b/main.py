#!/usr/bin/env python3

import math

x = int(input())

count = 0
value = 100
while(1):
    # for i in range(100):
    count += 1
    value = math.floor(value*1.01)
    # print(value)
    if value >= x:
        break
print(count)
