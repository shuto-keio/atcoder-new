#!/usr/bin/env python3
import fractions


def lcm(A):
    value = A[0]
    for i in range(1, len(A)):
        value = value * A[i] // fractions.gcd(value, A[i])
    return value


A = list(map(int, input().split()))

print(lcm(A))
