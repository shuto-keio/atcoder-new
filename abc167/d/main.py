#!/usr/bin/env python3
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
 
visit_check = [0 for i in range(len(a))]
 
pos=0
root = []
while(1):
    if visit_check[pos]==0:
        visit_check[pos]=1
        root.append(pos)
    else:
        loop_index = root.index(pos)
        if loop_index==0:
            root_one = []
            root_loop = root
        else:
            root_one = root[:loop_index]
            root_loop = root[loop_index:]
        break
    pos = a[pos]-1
 
if k+1<=len(root_one):
    ans = root_one[k]+1
else:
    k = k-len(root_one)
    index = k%len(root_loop)
    ans = root_loop[index]+1
# print(root_one)
# print(root_loop)
print(ans)