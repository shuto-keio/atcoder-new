#!/usr/bin/env python3

import queue
k = int(input())

q = queue.Queue()

for i in range(1, 10):
    q.put(i)

for i in range(k):
    tmp = q.get()
    if tmp % 10 != 0:
        q.put(10*tmp + tmp % 10 - 1)
    q.put(10*tmp + tmp % 10)
    if tmp % 10 != 9:
        q.put(10*tmp + tmp % 10 + 1)
print(tmp)
