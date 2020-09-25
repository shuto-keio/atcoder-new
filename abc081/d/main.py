#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

a_origin = a[:]

min_a = min(a)
min_a_index = a.index(min_a)
max_a = max(a)
max_a_index = a.index(max_a)

ans = []
if min_a < 0 and max_a > 0:

    if abs(min_a) > abs(max_a):
        a_new = []
        for i in range(len(a)):
            if a[i] > 0:
                a_new.append(a[i]+min_a)
                ans.append((min_a_index+1, i+1))
            else:
                a_new.append(a[i])
    else:
        a_new = []
        for i in range(len(a)):
            if a[i] < 0:
                a_new.append(a[i]+max_a)
                ans.append((max_a_index+1, i+1))
            else:
                a_new.append(a[i])

    # print(a_new)
    # print(ans)
    a = a_new

min_a = min(a)
max_a = max(a)

if min_a >= 0 and max_a >= 0:
    a_new = [a[0]]
    for i in range(1, len(a)):
        a_new.append(a[i]+a_new[-1])
        ans.append((i-1+1, i+1))
elif min_a <= 0 and max_a <= 0:
    a_new = [a[-1]]
    for i in reversed(range(0, len(a)-1)):
        a_new.append(a[i]+a_new[-1])
        ans.append((i+1+1, i+1))
    a_new = list(reversed(a_new))

# print(a_new)
# print(ans)
print(len(ans))
for i in ans:
    print(*i)


# for i, j in ans:
#     a_origin[j-1] += a_origin[i-1]
# print(a_new)
# print(a_origin)
