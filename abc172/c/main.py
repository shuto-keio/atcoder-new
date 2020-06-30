#!/usr/bin/env python3

import itertools
import bisect

n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum_ = 0
count = 0
for i in range(len(a)):
    if (sum_+a[i]) > k:
        break
    else:
        count += 1
        sum_ += a[i]
a_max = count

sum_ = 0
count = 0
for i in range(len(b)):
    if (sum_+b[i]) > k:
        i = i-1
        break
    else:
        count += 1
        sum_ += b[i]
b_max = count


list_ = list(reversed(a[:a_max])) + b[:b_max]
list_acc = list(itertools.accumulate(list_))


index = bisect.bisect_right(list_acc, k)
ans = index

now_left = 0
now_right = index


# print(list_)
while(now_right != len(list_)):
    k += list_[now_left]
    now_left += 1

    while(now_right != len(list_)):
        if list_acc[now_right] <= k:
            now_right += 1
        else:
            break
    # print(ans)
    ans = max(ans, now_right-now_left)

print(ans)
