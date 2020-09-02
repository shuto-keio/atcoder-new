#!/usr/bin/env python3

abc = list(map(int, input().split()))

abc.sort()

diff1 = abc[2]-abc[0]
diff2 = abc[2]-abc[1]

if (diff1+diff2) % 2 == 0:
    print((diff1+diff2)//2)
else:
    print((diff1+diff2+3)//2)
