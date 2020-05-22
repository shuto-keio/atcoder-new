#!/usr/bin/env python3

s = list(str(input()))

for i in range(3):
    if s[i] == s[i+1]:
        print("Bad")
        exit()
print("Good")
