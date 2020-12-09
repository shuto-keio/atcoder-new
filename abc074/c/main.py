#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

a, b, c, d, e, f = list(map(int, input().split()))

i = 0
dense = 0

ans = (a*100, 0)
for num_a in range(f//(100*a)+1):
    for num_b in range(f//(100*b)+1):

        if num_a == 0 and num_b == 0:
            continue

        water_mass = 100*(num_a*a+num_b*b)

        max_sugar = min(f-water_mass, water_mass//100*e)

        if max_sugar <= 0:
            continue

        sugar_mass = 0
        for num_c in range(0, max_sugar//c+1):
            num_d = (max_sugar - num_c*c)//d

            sugar_mass_tmp = num_c*c + num_d*d

            sugar_mass = max(sugar_mass, sugar_mass_tmp)

        dense_tmp = sugar_mass/(sugar_mass+water_mass)

        if dense < dense_tmp:
            ans = (water_mass+sugar_mass, sugar_mass)
            dense = dense_tmp

        # print(num_a, num_b, max_sugar)

print(*ans)
# print(dense)
