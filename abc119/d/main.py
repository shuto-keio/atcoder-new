#!/usr/bin/env python3
import bisect

a, b, q = list(map(int, input().split()))

s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]

x = [int(input()) for _ in range(q)]

s.sort()
t.sort()

i = 0


for i in range(len(x)):

    r_shrine = bisect.bisect_right(s, x[i])
    r_temple = bisect.bisect_right(t, x[i])

    l_shrine = r_shrine-1
    l_temple = r_temple-1

    # print(l_shrine, r_shrine)
    # print(l_temple, r_temple)

    ans = []
    if l_shrine >= 0 and l_temple >= 0:
        ans.append(max(x[i]-s[l_shrine], x[i]-t[l_temple]))  # <<
    if r_shrine < a and r_temple < b:
        ans.append(max(s[r_shrine]-x[i], t[r_temple]-x[i]))  # >>
    if l_shrine >= 0 and r_temple < b:
        min_ = min(x[i]-s[l_shrine], t[r_temple]-x[i])
        ans.append(min_+(t[r_temple]-s[l_shrine]))  # <>
    if r_shrine < a and l_temple >= 0:
        min_ = min(x[i]-t[l_temple], s[r_shrine]-x[i])
        ans.append(min_+(s[r_shrine]-t[l_temple]))  # <>

    print(min(ans))
