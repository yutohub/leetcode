# 0105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal

## 問題

2つの整数配列 preorder と inorder が与えられ、preorder は前置走査、inorder は後置走査を表しており、これらをもとにして二分木を構築して返す。

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

```
preorder (行きがけ順)

根からすべてのノードを反時計回りで囲むように一筆書きして、
ノードの左側を通った順番が行きがけ順になっている。
```

```
inorder (通りがけ順)

根からすべてのノードを反時計回りで囲むように一筆書きして、
ノードの下側を通った順番が行きがけ順になっている。

今回は使わないが重要な特徴として「二分探索木の場合、必ずデータの昇順となる」というものがある。
```

今回利用できる特徴としては、行きがけ順は「最初の値は必ず根ノードになっている」というものと、通りがけ順は「根ノードの値を境に左右の部分木に分けられる」というものがある。

preorder, inorder を受け取り、preorder の先頭の値を根ノードとする。inorder から先頭の値の位置を探し、その左右それぞれの部分に分ける。preorder も inorder から取り出した部分の配列の長さをもとにして分割する。それをもとに根ノードの左部分と右部分を再帰で定義していく。

> 参考資料:  
> [うさぎでもわかる2分探索木　後編　2分探索木における4つの走査方法](https://www.momoyama-usagi.com/entry/info-algo-tree-traverse#__preorder)