# 0349_Intersection_of_Two_Arrays

## 問題

2つの整数配列 nums1, nums2 が与えられたとき、それらの共通している要素を返す。

## 関連知識

### HashMap

`Map` とは `Key` と `Value` を紐付けてデータを格納するデータ構造のことで、`Key` の重複が許されておらず、`Key` から `Value` を参照するような時に使われる。特定の `Key` が登録されているか1つずつ調べるのは効率的でないので、ハッシュテーブルを使った実装になっており、ハッシュ関数により特定の `Key` に対して出来るだけ一意の値を返すため、全てを調べる必要がなく効率的である。

### collections.defaultdict

汎用の `Python` 組み込みコンテナ `dict` の代わりに、[collections.defaultdict](https://docs.python.org/ja/3.10/library/collections.html) を使うこともできる。`defaultdict` では存在しない  `Key` が入ってもデフォルト値を生成することができるため、状況によってはコードを簡略化することができる。

### Set

`Python` には、[set](https://docs.python.org/ja/3/tutorial/datastructures.html#sets) (集合) を扱うためのデータ型がある。集合とは、重複する要素をもたない、順序づけられていない要素の集まりである。`set` は、数学的な演算もサポートしています。空集合を作成するためには `set()` を使用しなければならず、`{}` だと空の辞書を作成してしまう。

## 解法

重複する要素がある配列から集合に型変換をして、その集合どうしの共通要素を取得するようにする。
