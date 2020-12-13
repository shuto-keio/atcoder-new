#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

# if n == 1:
#     if a[0] % 4 == 0:
#         print("Yes")
#         exit()
#     else:
#         print("No")
# if n == 2:
#     if a[0]*a[1] % 4 == 0:
#         print("Yes")
#         exit()
#     else:
#         print("No")
#         exit()


m_4 = 0
m_2 = 0
for i in a:
    if i % 4 == 0:
        m_4 += 1
    elif i % 2 == 0:
        m_2 += 1

other = n-m_4-m_2

if m_4 >= other:
    print("Yes")
elif (m_4+1) == other:
    if m_2 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
