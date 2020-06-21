#!/usr/bin/env python3

n = int(input())
a = list(map(int, input().split()))
q = int(input())


sum_a = sum(a)
a_dict = {i: 0 for i in set(a)}
for i in a:
    a_dict[i] += 1

for i in range(q):
    b, c = list(map(int, input().split()))
    if not b in a_dict:
        print(sum_a)
        continue
    num = a_dict[b]
    sum_a -= num*b
    sum_a += num*c
    print(sum_a)
    a_dict[b] = 0
    if c in a_dict:
        a_dict[c] += num
    else:
        a_dict[c] = num
