#!/usr/bin/env python3

import bisect
n, m, x = list(map(int, input().split()))
a = list(map(int, input().split()))

index = bisect.bisect_left(a, x)

ans = min(len(a[:index]), len(a[index:]))

print(ans)
