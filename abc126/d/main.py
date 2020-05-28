#!/usr/bin/env python3

n = int(input())

tree = [[] for _ in range(n)]
for i in range(n-1):
    u, v, w = list(map(int, input().split()))
    u, v = u-1, v-1

    tree[u].append((v, w))
    tree[v].append((u, w))

check = [0 for _ in range(n)]
color = [-1 for _ in range(n)]
color[0] = 0
check[0] = 1


queue = [0]
while(len(queue) > 0):
    index = queue.pop()
    tree_tmp = tree[index]
    for next_, weight in tree_tmp:
        # print(color)
        if color[next_] == -1:
            if weight % 2 == 0:
                color[next_] = color[index]
            else:
                color[next_] = (color[index]+1) % 2
            queue.append(next_)

for i in color:
    print(i)
