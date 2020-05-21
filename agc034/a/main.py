#!/usr/bin/env python3

n, a, b, c, d = list(map(int, input().split()))
s = list(str(input()))

start = a-1
end = c-1
sharp_count = 0
for i in range(start+1, (end-1)+1):
    if s[i] == "#" and s[i] == s[i+1]:
        print("No")
        exit()

start = b-1
end = d-1
sharp_count = 0
for i in range(start+1, (end-1)+1):
    if s[i] == "#" and s[i] == s[i+1]:
        print("No")
        exit()

if d < c:
    start = b-1
    end = d-1

    flag = 0
    for i in range(start, end+1):
        if s[i-1] == "." and (s[i-1] == s[i]) and (s[i] == s[i+1]):
            flag = 1
    if flag == 0:
        print("No")
        exit()

# if c == d:
#     print("No")
#     exit()
# elif c < b:
#     start = a-1
#     end = c-1

#     sharp_count = 0
#     for i in range(start+1, (end-1)+1):
#         if s[i] == "#" and s[i] == s[i+1]:
#             print("No")
#             exit()

#     start = b-1
#     end = d-1

#     sharp_count = 0
#     for i in range(start+1, (end-1)+1):
#         if s[i] == "#" and s[i] == s[i+1]:
#             print("No")
#             exit()
# elif c < d:
#     start = a-1
#     end = d-1

#     sharp_count = 0
#     for i in range(start+1, (end-1)+1):
#         if s[i] == "#" and s[i] == s[i+1]:
#             print("No")
#             exit()
# elif d < c:
#     start = a-1
#     end = c-1

#     sharp_count = 0
#     for i in range(start+1, (end-1)+1):
#         if s[i] == "#" and s[i] == s[i+1]:
#             print("No")
#             exit()

#     start = b-1
#     end = d-1
#     dot_count = 0
#     count = 0
#     for i in range(start-1, (end+1)+1):
#         if s[i] == ".":
#             count += 1
#         else:
#             dot_count = max(dot_count, count)
#             count = 0
#     if dot_count <= 2:
#         print("No")
#         exit()
print("Yes")
