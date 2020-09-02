#!/usr/bin/env python3

a, b = list(map(int, input().split()))
# print(a, b)

a -= 1
b -= 1
wide = 100

ans1 = [["#"]*wide for i in range(wide//2)]

ans2 = [["."]*wide for i in range(wide//2)]

index_x = 0
index_y = 0
while(a > 0):
    ans1[index_y][index_x] = "."
    index_x += 2
    if index_x == wide:
        index_x = 0
        index_y += 2
    a -= 1


index_x = 0
index_y = 1
a = b
while(a > 0):
    ans2[index_y][index_x] = "#"
    index_x += 2
    if index_x == wide:
        index_x = 0
        index_y += 2
    a -= 1

print(100, 100)
for i in ans1+ans2:
    print("".join(i))
