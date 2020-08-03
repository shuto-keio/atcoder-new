#!/usr/bin/env python3

s = str(input())

flag = 1
if s[0] != "A":
    flag = 0


num_C = 0
for i in s[2:-1]:
    if i == "C":
        num_C += 1

for i in s[1:]:
    if i != "C" and i.isupper():
        flag = 0

if num_C != 1:
    flag = 0


if flag == 0:
    print("WA")
else:
    print("AC")
