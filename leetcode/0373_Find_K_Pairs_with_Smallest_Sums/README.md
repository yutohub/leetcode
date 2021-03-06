# 0373_Find_K_Pairs_with_Smallest_Sums

## 問題

昇順でソートされた2つの整数配列 nums1, nums2 から一つずつ要素を取り出し、和が最も小さい k 組のペア (u1, v1) を返す。

## 関連知識

### Heap, Priority Queue

ヒープは優先度付きキューの実装の1つで、優先度付きキューは含まれる要素が何らかの優先度順に取り出されるという特徴を持っている。新たな要素を追加しても全体をソートすることなく優先度順を保つことができる。n番目に大きい要素が欲しいときなどに使える。

### heapq

優先度付きキューは [heapq](https://docs.python.org/ja/3/library/heapq.html) として標準ライブラリに用意されている。後から要素が追加され、その度に最大 or 最小の要素を早く取り出したい場合に使われる。

```python
import heapq
h = []                         # リストを用意しておく
heapq.heapify(h)               # リストをヒープに変換 (空なら不要)
heapq.heappush(h, 5)           # ヒープに要素追加
n = heapq.heappop(h)           # ヒープから最小値のpop
n = heapq.heappushpop(heap, 6) # pushしたあとにpopできる
n = heapq.heapreplace(heap, 7) # popしたあとにpushできる
```

## 解法

ソート済みのリストが入力なので下に行くほど大きな値になる。
`(0, 0)` からはじまり、列方向に辿っていくが、
左端が採用されたときに行方法に辿ることで、効率の良い探索ができる。
優先度付きキューを採用し、常に一番小さいものを取り出して処理することで、
最も小さい k 組のペアを取り出すことができる。

|  | 2 | 4 | 6 |
|:---:|:---:|:---:|:---:|
| 1 | 3 | 5 | 7 |
| 7 | 9 | 11 | 13 |
| 11 | 13 | 15 | 17 |
