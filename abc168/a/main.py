#!/usr/bin/env python3

a = str(input())

if int(a[-1]) == 3:
    print("bon")
elif int(a[-1]) in [2, 4, 5, 7, 9]:
    print("hon")
else:
    print("pon")
