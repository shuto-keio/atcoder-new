#!/usr/bin/env python3
import datetime

s = str(input())

year = int(s[:4])
month = int(s[5:7])
day = int(s[8:10])

a = datetime.date(year, month, day)
b = datetime.date(2019, 4, 30)

if a <= b:
    print("Heisei")
else:
    print("TBD")
