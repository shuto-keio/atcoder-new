#!/usr/bin/env python3

a, b, c = list(map(int, input().split()))

capa_a = a-b

if capa_a >= c:
    print(0)
else:
    print(c-capa_a)
