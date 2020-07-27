#!/usr/bin/env python3

from collections import Counter

n = int(input())
v = list(map(int, input().split()))


v_odd = []
v_even = []
for i in range(n):
    if i % 2 == 0:
        v_even.append(v[i])
    else:
        v_odd.append(v[i])

c_even = Counter(v_even).most_common()
c_odd = Counter(v_odd).most_common()

# print(c_even)
# print(c_odd)

if c_even[0][0] == c_odd[0][0]:
    if len(c_even) == 1:
        c_odd = c_odd[1:]
    elif len(c_odd) == 1:
        c_even = c_even[1:]
    else:
        if c_even[1][1] >= c_odd[1][1]:
            c_even = c_even[1:]
        else:
            c_odd = c_odd[1:]

if len(c_even) == 0:
    c_even.append((-1, 0))
if len(c_odd) == 0:
    c_odd.append((-1, 0))

diff_even = n//2-c_even[0][1]
diff_odd = n//2-c_odd[0][1]

print(diff_even+diff_odd)
