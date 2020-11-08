#!/usr/bin/env python3
from collections import Counter
import sys
sys.setrecursionlimit(10**6)

s = [int(i) for i in str(input())]

if len(s) < 3:
    if len(s) == 1:
        if s[0] % 8 == 0:
            print("Yes")
            exit()
    if len(s) == 2:
        if (s[0]*10+s[1]) % 8 == 0:
            print("Yes")
            exit()
        if (s[1]*10+s[0]) % 8 == 0:
            print("Yes")
            exit()
    print("No")
    exit()

c1 = Counter(s)
for i in range(1, 10):
    if i not in c1:
        c1[i] = 0

# print(c1)

for i in range(13, 125):
    sample = i*8

    tmp = [int(i) for i in str(sample)]
    c2 = Counter(tmp)

    flag = 1
    for key, value in c2.items():

        if c1[key] < value:
            flag = 0
            break
    if flag == 1:
        # print(sample)
        print("Yes")
        exit()

print("No")
