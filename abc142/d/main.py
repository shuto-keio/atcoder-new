#!/usr/bin/env python3

# a = int(input())
a, b = list(map(int, input().split()))
# a = list(str(input()))

# com_div_list_min = [1]
# com_div_list_max = []
# if a%2==0 and b%2==0:
#     com_div_list_min.append(2)

if a != 1:
    diva_list_min = []
    diva_list_max = []
    count = 1
    while(count <= a**0.5):
        if a % count == 0:
            diva_list_min.append(count)
            diva_list_max.append(a//count)
        count += 1

    diva_list_max.reverse()
    div_a = diva_list_min+diva_list_max
else:
    div_a = [1]

com_div_ab = []
for i in (div_a):
    if b % i == 0:
        com_div_ab.append(i)


if com_div_ab == [1]:
    print(1)
    exit()

count = 1
while(count < len(com_div_ab)):
    new_com_div_ab = com_div_ab[:count+1]
    num = new_com_div_ab[-1]

    for i in range(count+1, len(com_div_ab)):
        if com_div_ab[i] % num != 0:
            new_com_div_ab.append(com_div_ab[i])
    # print(com_div_ab)
    # print(new_com_div_ab)
    # print()
    com_div_ab = new_com_div_ab
    count += 1


print(len(new_com_div_ab))
