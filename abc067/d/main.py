#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())

data = [[] for i in range(n)]

for i in range(n-1):
    a, b = list(map(int, input().split()))
    data[a-1].append(b-1)
    data[b-1].append(a-1)


visit = [0]*n


def search_shortest_path(now):
    visit[now] = 1
    routes = data[now]

    for i in routes:
        if i == (n-1):
            return [n-1, now]
        if visit[i] == 1:
            continue
        path = search_shortest_path(i)
        if path is not None:
            path.append(now)
            return path


path = search_shortest_path(0)
shortest_path = list(reversed(path))


# shortest_path = [0, 3, 6]
# shortest_path = [0, 3]
ans = [-1]*n
index0_all = []
index1_all = []
for i in range(len(shortest_path)//2):
    index0 = shortest_path[i]
    index1 = shortest_path[-i-1]
    ans[index0] = 0
    ans[index1] = 1
    index0_all.append(index0)
    index1_all.append(index1)
if len(shortest_path) % 2 == 1:
    index0 = shortest_path[len(shortest_path)//2]
    ans[index0] = 0
    index0_all.append(index0)

# print(index0)
# print(index1)

for index0 in index0_all:
    tmp = data[index0]
    for i in tmp:
        if ans[i] == -1:
            ans[i] = 0
            index0_all.append(i)


for index1 in index1_all:
    tmp = data[index1]
    for i in tmp:
        if ans[i] == -1:
            ans[i] = 1
            index1_all.append(i)

num_Fennec = 0
num_Snuke = 0
for i in ans:
    if i == 0:
        num_Fennec += 1
    elif i == 1:
        num_Snuke += 1
    else:
        raise("Error")

# print(ans)
if num_Snuke >= num_Fennec:
    print("Snuke")
else:
    print("Fennec")
