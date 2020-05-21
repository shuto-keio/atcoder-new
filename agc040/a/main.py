#!/usr/bin/env python3
s = list(str(input()))

n = len(s)+1


from_left = [0 for _ in range(n)]
from_right = [0 for _ in range(n)]

for i, sym in enumerate(s, 1):
    if sym == ">":
        from_left[i] = 0
    else:
        from_left[i] = from_left[i-1]+1

for i, sym in enumerate(s[::-1]):
    i = n-2-i
    if sym == "<":
        from_right[i] = 0
    else:
        from_right[i] = from_right[i+1]+1

seq = [max(x, y) for x, y in zip(from_left, from_right)]

print(sum(seq))
