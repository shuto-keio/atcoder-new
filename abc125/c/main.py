#!/usr/bin/env python3

import fractions

n = int(input())
a = list(map(int, input().split()))


left_gcd = [0 for _ in range(n)]
right_gcd = [0 for _ in range(n)]

left_gcd[0] = a[0]
right_gcd[-1] = a[-1]

for i in range(1, n):
    left_gcd[i] = fractions.gcd(left_gcd[i-1], a[i])

for i in range(n-2, -1, -1):
    right_gcd[i] = fractions.gcd(right_gcd[i+1], a[i])
# print(left_gcd)
# print(right_gcd)

ans = 1
for i in range(1, n-1):
    num1 = left_gcd[i-1]
    num2 = right_gcd[i+1]
    ans = max(ans, fractions.gcd(num1, num2))

ans = max(ans, right_gcd[1], left_gcd[-2])
print(ans)
