#!/usr/bin/env python3

k = int(input())

now = 1
step = 1


def sunuke(n):
    r = 0
    while n:
        r += n % 10
        n //= 10
    return r


def ok(a, b):
    return a * sunuke(b) <= b*sunuke(a)


while k:
    if ok(now, now+step):
        print(now)
        k -= 1
        now += step
    else:
        nstep = step*10
        while now % nstep != nstep-1:
            now += step
        step = nstep
