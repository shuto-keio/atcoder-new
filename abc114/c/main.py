#!/usr/bin/env python3
import itertools

n = int(input())

must = set(["3", "5", "7"])
count = 0

for i in itertools.product("0357", repeat=10):
    num = int("".join(i))
    set_ = set(list(str(num)))
    if 0 in set_:
        continue
    if set_ != must:
        continue

    if int("".join(i)) <= n:
        # print(int("".join(i)))
        count += 1
    else:
        break
print(count)
