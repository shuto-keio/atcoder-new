#!/usr/bin/env python3
import heapq
# import bisect

n, m = list(map(int, input().split()))
a = list(map(lambda x: int(x)*(-1), input().split()))

heapq.heapify(a)
for i in range(m):
    value = heapq.heappop(a)
    value = (value+1)//2
    heapq.heappush(a, value)

# print(a)
print(-sum(a))
