#!/usr/bin/env python3
from collections import deque

H, W = list(map(int, input().split()))
ch, cw = list(map(int, input().split()))
dh, dw = list(map(int, input().split()))

ch -= 1
cw -= 1
dh -= 1
dw -= 1

S = [list((str(input()))) for i in range(H)]


def check(h, w):
    if h < 0 or h >= H:
        return False
    if w < 0 or w >= W:
        return False
    if S[h][w] == "#":
        return False
    return True


def main():

    map_ = [[10**10]*W for i in range(H)]
    # map_[ch][cw] = 0

    dq = deque([[ch, cw, 0]])

    while(len(dq) > 0):
        # print(dq)
        h, w, value = dq.popleft()
        map_value = map_[h][w]
        if map_value <= value:
            continue
        map_[h][w] = value

        for i in [-2, -1, 0, 1, 2]:
            for j in [-2, -1, 0, 1, 2]:
                if i == 0 and j == 0:
                    continue
                if abs(i)+abs(j) == 1:
                    if check(h+i, w+j):
                        # print(h+i, w+)
                        if map_[h+i][w+j] > value:
                            dq.appendleft([h+i, w+j, value])
                else:
                    if check(h+i, w+j):
                        if map_[h+i][w+j] > value+1:
                            dq.append([h+i, w+j, value+1])
    # for i in map_:
        # print(i)
    ans = map_[dh][dw]
    if ans == 10**10:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
