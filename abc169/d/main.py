#!/usr/bin/env python3
import collections


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    if arr[0] == [1, 1]:
        return []

    return arr


n = int(input())
fact_list = factorization(n)

# print(fact_list)
ans = 0
for num, exp in fact_list:

    for i in range(1, exp+1):
        if exp-i >= 0:
            ans += 1
            exp -= i
        else:
            break

print(ans)
