# atcoder-new

# np.uniqueの代わりに
https://note.nkmk.me/python-collections-counter/
https://atcoder.jp/contests/abc159/submissions/11711787

# 二分探索
bisect
https://qiita.com/ta7uw/items/d6d8f0ddb215c3677cd3
https://atcoder.jp/contests/abc130/submissions/5943353

# 優先度付きキュー
- 最大値の取得、要素の挿入がリストと比べて早い
  - n >> log(n)
https://atcoder.jp/contests/abc141/tasks/abc141_d
https://qiita.com/ell/items/fe52a9eb9499b7060ed6

# 最大公約数
```
from math import gcd
gcd(a,b)
```

# 最小公倍数
```
from math import gcd
def lcm(a,b):
    return a//gcd(a,b)*b
```

# [[1,2],[2,3],[3.4]]のようなリストの[i][1]を基準にソート¶
value = sorted(value, key=lambda x: x[1])

# 素因数分解
```
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
```


# Python PyPyの比較
https://qiita.com/OKCH3COOH/items/f0c5c4681bc30dddf7f4
基本的に、リストの生成、再帰関数以外はPyPyの方が早い

# Union-Find
https://note.nkmk.me/python-union-find/

# 二部グラフの最大マッチング問題
https://atcoder.jp/contests/abc091/tasks/arc092_a
http://ina17.hatenablog.jp/entry/2017/11/29/184345

# Segment Tree
https://qiita.com/takayg1/items/c811bd07c21923d7ec69

# Lazy Segment Tree
https://qiita.com/takayg1/items/b7b3f7d458915bcc7a4e


# 編集距離
http://nw.tsuda.ac.jp/lec/EditDistance/