#!/usr/bin/env python3
import itertools


n = int(input())

list_26 = [26]
while list_26[-1] < 1000000000000001:
    list_26.append(list_26[-1]*26)

list_26 = list(itertools.accumulate(list_26))
# print(list_26)

for i in range(len(list_26)):
    if n <= list_26[i]:
        break
digit = i

if i != 0:
    n -= list_26[i-1]
# print(n)

n -= 1


def base_10_to_n(x, n):
    x_dummy = x
    out = []
    while x_dummy > 0:
        out.append(int(x_dummy % n))
        x_dummy = int(x_dummy/n)
    if out == []:
        return [0]
    return out


ans = base_10_to_n(n, 26)

ans += [0]*(i+1-len(ans))
ans.reverse()

for i in ans:
    print(chr(i+97), end="")
print()
# print(ans)


# ans = base_10_to_n(n, 26)
# ans.reverse()

# for i in ans:
#     if
# print(ans)
