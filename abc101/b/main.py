#!/usr/bin/env python3

n = int(input())

sum_ = 0
for i in str(n):
    sum_ += int(i)

if n % sum_ == 0:
    print("Yes")
else:
    print("No")
