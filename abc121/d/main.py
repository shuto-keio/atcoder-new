#!/usr/bin/env python3

a, b = list(map(int, input().split()))

if b-a == 0:
    print(a)
    exit()
if b-a == 1:
    print(a ^ b)
    exit()

list_ = []
ans = 0
if a % 2 != 0:
    list_.append(a)
    a += 1

if b % 2 == 0:
    list_.append(b)
    b -= 1

num = ((b+1)-a)//2
if num % 2 == 0:
    ans = 0
else:
    ans = 1


for i in list_:
    ans = ans ^ i
print(ans)
