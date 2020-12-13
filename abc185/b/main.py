#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n, m, t = list(map(int, input().split()))

ab = [0]
for i in range(m):
    a, b = list(map(int, input().split()))
    ab.append(a)
    ab.append(b)
ab.append(t)

# print(ab)

now = n
for i in range(1, len(ab)):
    pre = ab[i-1]
    post = ab[i]
    if i % 2 == 1:
        now -= post-pre
        if now <= 0:
            print("No")
            exit()
    else:  # charge
        now += post-pre
        now = min(n, now)
    # print(now)

print("Yes")
