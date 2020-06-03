#!/usr/bin/env python3

s = list(str(input()))

count_0 = 0
count_1 = 0
for i in s:
    if i == "0":
        count_0 += 1
    else:
        count_1 += 1

print(min(count_0, count_1)*2)
