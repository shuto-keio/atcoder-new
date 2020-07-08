#!/usr/bin/env python3
# from collections import Counter
s = list(str(input()))
t = list(str(input()))

dict_ = {}
for i in range(len(s)):
    if s[i] in dict_:
        dict_[s[i]].append(i)
    else:
        dict_[s[i]] = [i]
for key, value in dict_.items():
    a = set([])
    for i in value:
        a.add(t[i])
    # print(a)
    if len(set(a)) != 1:
        print("No")
        exit()

s, t = t, s
dict_ = {}
for i in range(len(s)):
    if s[i] in dict_:
        dict_[s[i]].append(i)
    else:
        dict_[s[i]] = [i]
for key, value in dict_.items():
    a = set([])
    for i in value:
        a.add(t[i])
    # print(a)
    if len(set(a)) != 1:
        print("No")
        exit()
print("Yes")
