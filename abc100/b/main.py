#!/usr/bin/env python3

d, n = list(map(int, input().split()))

if n == 100:
    if d == 0:
        print(100+1)
    elif d == 1:
        print(100*100+100)
    else:
        print(100*10000+10000)
else:
    if d == 0:
        print(n)
    else:
        print((100**d)*n)
