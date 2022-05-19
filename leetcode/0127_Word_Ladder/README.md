# 0127_Word_Ladder

## 問題

beginWord と endWord の2つの単語と wordList が与えられたとき、beginWord から endWord への最短で変換するのに必要な単語の数を返す、変換できるのは1文字違いの単語のみで、beginWord のみ wordList に存在する必要はない。

## 関連知識

### 探索アルゴリズム

探索アルゴリズムでスタック（後に入れたものが先に出る）を使うかキュー（先に入れたものが先に出る）を使うかによって、深さ優先探索（スタック使用）か幅優先探索（キュー使用）になる。

### BFS

`BFS`（幅優先探索）は、`Graph` の探索に用いられるアルゴリズムで、最小移動手数を求めるような出来るだけ根から近い部分を積極的に探索した方が効率が良いときに用いる。

### DFS

`DFS`（深さ優先探索）は、`Graph` の探索に用いられるアルゴリズムで、スタートからゴールまで辿り着けるかを調べる問題のように、一度最後のノードまで探索した方が効率の良いときに用いる。

### 使い分け

`DFS`（深さ優先探索）は再起を使って比較的簡単に書けるため、全て列挙する場合は`DFS`（深さ優先探索）を用いることが多い。最短路や最小手数などを求める場合は `BFS`（幅優先探索）の方が有効である。

## 解法

ポイントとなるのは、どのように1文字違いかどうか判定するかになる。全ての単語に対して、1文字を `*` に置き換えた文字を `Key` とし、もとの単語を `Value` をした辞書を作成しておく。これにより `*ot` を検索したときに、`dot`, `lot` に移動可能であることが判断できるようになる。また、最短経路を求めるということで考えなくてはいけないのが、一度進んだ場所には進まないように記録しておくことと、幅優先探索にすることである。

```
beginWord = "hit", endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

"hit" - "hot" --- "dot" - "dog" --- "cog"
               |    |       |    |
               -- "lot" - "log" --
```