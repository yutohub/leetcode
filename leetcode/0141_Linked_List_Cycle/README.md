# 0141_Linked_List_Cycle

## 問題

連結リストにサイクル（循環）が存在するかどうかを判定する。

## 関連知識

### 配列
```
データアクセス O(1) 
データ挿入/削除 O(n)
各要素に何番目かインデックスをつけているため何番目か指定するだけでアクセスできるが、
途中の部分に変更を加えると残りの部分のインデックスを変える必要がある。
```

### 連結リスト
```
データアクセス O(n)
データ挿入/削除 O(1)
各要素には次の要素を指し示すポインタしか含まれていないため辿っていく必要があるが、
途中の部分に変更を加えても前後にしか影響が及ばない。
```

## 解法

連結リストを一つずつ辿っていく`slow`と、一つ飛ばしで辿っていく`fast`を用意して、`slow`と`fast`が同じポインタを示すかどうか判断する。