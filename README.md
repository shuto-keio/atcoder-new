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
import fractions
value = A[0]
for i in range(1, N):
    value = fractions.gcd(value, A[i])
print(value)
```

# 最小公倍数
```
import fractions
value = A[0]
for i in range(1, N):
    value = value * A[i] // fractions.gcd(value, A[i])
print(value)
```

# [[1,2],[2,3],[3.4]]のようなリストの[i][1]を基準にソート¶
value = sorted(value, key=lambda x: x[1])

# Python PyPyの比較
https://qiita.com/OKCH3COOH/items/f0c5c4681bc30dddf7f4
基本的に、リストの生成、再帰関数以外はPyPyの方が早い
