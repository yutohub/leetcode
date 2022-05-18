# 0001_Two_Sum

## 問題

整数 nums の配列と整数 target が与えられたとき、2つの数値の和が target になるようなインデックスを返せ。

## 関連知識

### HashMap

`Map` とは `Key` と `Value` を紐付けてデータを格納するデータ構造のことで、`Key` の重複が許されておらず、`Key` から `Value` を参照するような時に使われる。特定の `Key` が登録されているか1つずつ調べるのは効率的でないので、ハッシュテーブルを使った実装になっており、ハッシュ関数により特定の `Key` に対して出来るだけ一意の値を返すため、全てを調べる必要がなく効率的である。

### collections.defaultdict

汎用の `Python` 組み込みコンテナ `dict` の代わりに、[collections.defaultdict](https://docs.python.org/ja/3.10/library/collections.html) を使うこともできる。`defaultdict` では存在しない  `Key` が入ってもデフォルト値を生成することができるため、状況によってはコードを簡略化することができる。

```python
d = collections.defaultdict(int)  # 初期値: 0
d = collections.defaultdict(list) # 初期値: []
d = collections.defaultdict(dict) # 初期値: {}
d = collections.defaultdict(bool) # 初期値: False

# 出現数のカウントには collections.Counter があるが、こちらでも実装できる。
strings = "abcded"
counter = collections.defaultdict(int)
for s in strings:
    counter[s] += 1
# {'a': 1, 'b': 1, 'c': 1, 'd': 2, 'e': 1})

# 特に list や dict などで初期化するときに if 文で条件分岐を省略できる
default_dict = collections.defaultdict(list)
words = ["I", "like", "what", "I", "like"]
for i, word in enumerate(words):
    default_dict[word].append(i)
# {'I': [0, 3], 'like': [1, 4], 'what': [2]})
```

## 解法

全ての組み合わせを計算すると時間がかかるため `num` と `target` の差を `Key` とし、その `index` を `Value` として `HashMap` に登録しておき、`num` が `Key` として存在するか調べることで、ペアを見つけることができる。