#!/usr/bin/env python3

n = int(input())


pn = [2, ]
A = 3000
for L in range(5, A):
    chk = True
    for L2 in pn:
        if L % L2 == 0:
            chk = False
    if chk:
        pn.append(L)
# print(pn)

for i in pn:
    if i % 5 == 2:
        print(i, "", end="")
        n -= 1
    if n == 0:
        exit()


# print(*ans)
