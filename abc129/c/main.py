#!/usr/bin/env python3

n, m = list(map(int, input().split()))

if m != 0:
    a = [int(input()) for _ in range(m)]
else:
    a = [-1]

mod = 1000000007

if n == 1:
    print(1)
    exit()
elif n == 2:
    if a[0] == 1:
        print(1)
    else:
        print(2)
    exit()


if a[0] == 1:
    a_2, a_1 = 1, 0
    index = 1
else:
    a_2, a_1 = 1, 1
    index = 0

for i in range(2, n+1):
    if index < len(a):
        if i == a[index]:
            a_now = 0
            index += 1
            a_1, a_2 = a_now, a_1
            continue

    a_now = (a_1+a_2) % mod
    # print(a_now)
    a_1, a_2 = a_now, a_1
    # print(a_now)
print(a_now % mod)

# 0, 1, 2, 3, 4, 5, 6

# 1, 1, 2, 0, 2, 2, 4
