#!/usr/bin/env python3

n, m = list(map(int, input().split()))
x = list(map(int, input().split()))

if n >= m:
    print(0)
    exit()

x.sort()

diff = [x[i+1]-x[i] for i in range(m-1)]

diff.sort()


print(sum(diff[:m-n]))
