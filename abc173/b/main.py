#!/usr/bin/env python3

n = int(input())

dict_ = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}

for _ in range(n):
    s = str(input())
    dict_[s] += 1


print("AC x {}".format(dict_["AC"]))
print("WA x {}".format(dict_["WA"]))
print("TLE x {}".format(dict_["TLE"]))
print("RE x {}".format(dict_["RE"]))
