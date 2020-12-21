#!/usr/bin/env python3
import heapq
import sys
sys.setrecursionlimit(10**6)


n = int(input())
a = list(map(int, input().split()))

a1 = a[:n]
a2 = [-i for i in a[2*n:]]
# print(a1)
# print(a2)


# a1.sort()
# a2.sort()
heapq.heapify(a1)
heapq.heapify(a2)

sum_a1 = sum(a1[0:n])
sum_a2 = sum(a2[0:n])

data_a1 = [sum_a1]
for i in range(n, 2*n):
    value = a[i]
    # a2
    value2 = heapq.heappop(a1)
    if value > value2:
        heapq.heappush(a1, value)
        sum_a1 = sum_a1 + value - value2
    else:
        heapq.heappush(a1, value2)

    data_a1.append(sum_a1)
# print(data_a1)


data_a2 = [sum_a2]
for i in reversed(range(n, 2*n)):
    value = -a[i]
    # a2
    value2 = heapq.heappop(a2)
    if value > value2:
        heapq.heappush(a2, value)
        sum_a2 = sum_a2 + value - value2
    else:
        heapq.heappush(a2, value2)

    data_a2.append(sum_a2)

data_a2.reverse()
# print(data_a2)

ans = data_a1[0]+data_a2[0]
for i in range(1, len(data_a1)):
    ans_tmp = data_a1[i]+data_a2[i]
    ans = max(ans, ans_tmp)
print(ans)
