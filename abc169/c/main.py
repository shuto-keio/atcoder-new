#!/usr/bin/env python3

a, b = list(map(str, input().split()))

a = int(a)
b_1 = int(b[:-3])*100
b_2 = int(b[-2:])

# print(b_1)
# print(b_2)

print(a*(b_1+b_2)//100)
