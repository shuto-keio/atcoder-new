#!/usr/bin/env python3

from fractions import gcd

a, b, c, d = list(map(int, input().split()))


def calc(min_, max_, div_num):
    if (min_ % div_num) != 0:
        min_ = min_ - (min_ % div_num)+div_num

    if min_ > max_:
        return 0
    return (max_-min_)//div_num+1


# print(calc(a, b, c))
# print(calc(a, b, d))
# print(calc(a, b, c*d//gcd(c, d)))
print((b-a+1)-(calc(a, b, c)+calc(a, b, d)-calc(a, b, c*d//gcd(c, d))))
