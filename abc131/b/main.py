#!/usr/bin/env python3

n, l = list(map(int, input().split()))

max_ = l+n-1
min_ = l

# print(min_, max_)
if max_ >= 0 and min_ <= 0:
    print((max_+min_)*(max_-min_+1)//2)
elif max_ <= 0:
    max_ -= 1
    print((max_+min_)*(max_-min_+1)//2)
else:
    min_ += 1
    print((max_+min_)*(max_-min_+1)//2)
