# 0347_Top_K_Frequent_Elements

## 問題

整数配列numsと整数kが与えられたとき、最も頻度の高いk個の要素を返せ。答えはどのような順番で返してもよい。

## 関連知識

### collections.Counter

要素の頻度については、標準ライブラリ `collections` にある [Counter](https://docs.python.org/ja/3/library/collections.html#collections.Counter) クラスを用いる。仕様は `dict` に近く、要素を辞書のキーとして保存し、そのカウントを辞書の値として保存する。

```python
l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(l)
# Counter({'a': 4, 'c': 2, 'b': 1})
c.most_common(2) 
# [('a', 4), ('c', 2)]
```

### heapq.nlargest

リストの最大値・最小値から順にn個の要素を取得したい場合、 [heapq](https://docs.python.org/ja/3/library/heapq.html) を使う方法もある。要素を全て並び替える `sort` を用いるよりも、計算コストが少ない。

```python
l = [3, 6, 7, -1, 23, -10, 18]
heapq.nlargest(3, l)
# [23, 18, 7]
heapq.nsmallest(3, l)
# [-10, -1, 3]
```

## 解法

値の頻度を求めるため `collections.Counter` を用いて、頻度を計算する。最も頻度の高いk個の要素を求めるために `most_common` または `heapq.nlargest` を用いる。