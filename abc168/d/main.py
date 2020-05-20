#!/usr/bin/env python3

from collections import deque

n, m = list(map(int, input().split()))

road_map = [[] for _ in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    road_map[a-1].append(b-1)
    road_map[b-1].append(a-1)
# print(road_map)

check_list = [0 for _ in range(n)]
d = deque([(0, -1)])
ans = [0 for _ in range(n)]
while(len(d) >= 1):
    # print(d)
    index, origin = d.popleft()
    if check_list[index] == 1:
        continue
    else:
        check_list[index] = 1
        ans[index] = origin
    road_list = road_map[index]

    for i in road_list:
        if check_list[i] == 0:
            # check_list[i] = 1
            d.append((i, index))


for i in range(1, len(ans)):
    if ans[i] == -1:
        print("No")
        exit()

print("Yes")
for i in range(1, len(ans)):
    print(ans[i]+1)
