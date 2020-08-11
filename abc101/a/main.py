#!/usr/bin/env python3

s = str(input())

a = [1 if i == "+" else -1 for i in s]

print(sum(a))
