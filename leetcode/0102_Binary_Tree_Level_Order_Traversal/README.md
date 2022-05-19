# 0102_Binary_Tree_Level_Order_Traversal

## 問題

二分木のルートが与えられたとき、そのノードの深さごとに配列に分けて返す。

## 関連知識

### Binary Tree

`Binary Tree`（二分木）とは、データ構造の1つである。あるノードが持つ子の数が多くて2つであるものをいう。例えば、`Binary Search Tree`（二分探索）や `Heap`（ヒープ）を実装するために使われる。

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Binary Search Tree

`Binary Search Tree`（二分探索木）は、コンピュータプログラムにおいて、「左の値 ≤ 親の値 ≤ 右の値」という条件を持つ二分木である。

### BFS

`BFS`（幅優先探索）は、`Graph` の探索に用いられるアルゴリズムで、最小移動手数を求めるような出来るだけ根から近い部分を積極的に探索した方が効率が良いときに用いる。

### DFS

`DFS`（深さ優先探索）は、`Graph` の探索に用いられるアルゴリズムで、スタートからゴールまで辿り着けるかを調べる問題のように、一度最後のノードまで探索した方が効率の良いときに用いる。

### 使い方

`DFS`（深さ優先探索）は再起を使って比較的簡単に書けるため、全て列挙する場合は `DFS`（深さ優先探索）を用いることが多い。最短路や最小手数などを求める場合は `BFS`（幅優先探索）の方が有効である。

## 解法

ノードの深さ毎に分けるという目的には、同じ深さの層から優先的に探索する `BFS`（幅優先探索）を用いる。レベルを `Key` とし、ノードを `Value` とする辞書を作成する。それぞれのキューにノードとそのノードの深さを保存しておき、キューがなくなるまで繰り返す。