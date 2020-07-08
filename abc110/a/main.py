#!/usr/bin/env python3

abc = list(map(int, input().split()))

abc.sort()

print(abc[-1]*10+abc[0]+abc[1])
