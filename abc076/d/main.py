#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))


v_all = []
for i in range(n):
    v_all += [v[i]]*t[i]
# print(v_all)


max_speeds = [(0, 0, 0)]
for i in range(1, len(v_all)+1):
    limits1 = len(v_all)-i
    limits2 = v_all[i-1]
    limits3 = 10**10
    for j in range(i+1, len(v_all)):
        limits3 = min((j-i)+v_all[j]-1, limits3)
    # print(limits1, limits2, limits3)
    max_speeds.append((limits1, limits2, limits3))

max_speeds_n = [(0, 0, 0)]
for i in range(len(max_speeds)):
    x, y, z = max_speeds[i]
    if


speed = 0
speeds = []
for i in range(len(v_all)):
    limits1, limits2, limits3 = max_speeds[i]
    speed = min(speed+1, limits1, limits2, limits3)
    # print(speed, max_speeds[i])
    if speed < limits2 and speed < limits3 and (i+1) != len(v_all):
        # limits1, limits2, limits3 = max_speeds[i+1]
        limitsx = min(max_speeds[i+1])
        if limitsx == speed:
            speed += 0.25
        else:
            speed = min(speed, limits1, limits2, limits3)
        speeds.append(speed)
        speed = int(speed)
        continue

    speeds.append(speed)

# print(speeds)
print(sum(speeds))
# print(max_speeds)
