#!/usr/bin/env python3

s = str(input())

week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
week.reverse()

index = week.index(s)
print(index+1)
