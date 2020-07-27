#!/usr/bin/env python3

n = list(str(int(input())))

for i in range(len(n)):
    if n[i] == "9":
        n[i] = "1"
    elif n[i] == "1":
        n[i] = "9"

for i in n:
    print(i, end="")
