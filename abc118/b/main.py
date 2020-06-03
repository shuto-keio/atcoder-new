#!/usr/bin/env python3

k, m = list(map(int, input().split()))


set_ = set(range(1, m+1))


for i in range(k):
    _, *a = list(map(int, input().split()))
    set_ = set_ & set(a)


print(len(set_))
