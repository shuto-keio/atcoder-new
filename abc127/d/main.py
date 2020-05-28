#!/usr/bin/env python3
import heapq

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
bc = [list(map(int, input().split())) for _ in range(m)]

bc = sorted(bc, key=lambda x: x[1], reverse=True)
# print(bc)

heapq.heapify(a)
for b, c in bc:
    for i in range(b):
        num = heapq.heappop(a)
        if num < c:
            heapq.heappush(a, c)
        else:
            heapq.heappush(a, num)
            break
# print(a)
print(sum(a))
