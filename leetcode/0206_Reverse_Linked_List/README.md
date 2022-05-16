# 0206_Reverse_Linked_List

## 問題

与えられた連結リストを反転させたものを返す。

## 関連知識

### スタック

コンピュータで用いられる基本的なデータ構造の1つで、後に入れたものが先に出る構造になっている。

### キュー

コンピュータで用いられる基本的なデータ構造の1つで、先に入れたものが先に出る構造になっている。

### collections.deque

配列を使う代わりに標準ライブラリーとして用意されている [collections.deque](https://docs.python.org/ja/3/library/collections.html#collections.deque) が用いられる。
```python
from collections import deque
stack = deque([]) # 初期化
stack.append(x)   # xをの右側につけ加える
y = stack.pop()   # 右側から要素をひとつ削除してyに取り出す
z = queue.pop()   # 左側から要素をひとつ削除してzに取り出す
```

## 解法

スタックに取り出したものを一旦保存して、後に入れたものから取り出して連結リストに追加していく。