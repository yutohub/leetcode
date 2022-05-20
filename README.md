# LeetCode

LeetCodeの解答をまとめたいと思います。

## Solution

使用する予定の言語は `Python3` と `Go` です。

### LinkedList

連結リストはコンピュータで用いられる基本的なデータ構造の1つで、各要素が前や後ろの要素へのリンクを持っているような実装になっている。問題を解くには、参照渡しを理解しておく必要がある。

| # | Title | Solution | Summary |
|---|---|---|---|
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | [Python3](leetcode/0141_Linked_List_Cycle) | 連結リストにサイクル（循環）が存在するかどうかを判定する。 |
| 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | [Python3](leetcode/0142_Linked_List_Cycle_II) | 連結リストにサイクル（循環）が存在するかどうかを判定し、サイクルがある場合はサイクルが開始するノードを返す。 |
| 83 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | [Python3](leetcode/0083_Remove_Duplicates_from_Sorted_List) | ソートされた連結リストの重複を解消した連結リストを返す。 |
| 83 | [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | [Python3](leetcode/0082_Remove_Duplicates_from_Sorted_List_II) | ソートされた連結リストの重複を消去した連結リストを返す。 |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | [Python3](leetcode/0002_Add_Two_Numbers) | 2つ負でない整数を表す連結リストが渡される。数値は逆順で格納されている。2つの数値を加算した結果を連結リストとして返す。 |

### Stack

スタックはコンピュータで用いられる基本的なデータ構造の1つで、後に入れたものが先に出る構造になっている。似ているデータ構造の1つにキューがあり、キューは先に入れたものが先に出る構造になっている。問題を解くには配列を使うより [collections.deque](https://docs.python.org/ja/3/library/collections.html#collections.deque) を使うのが良い。

| # | Title | Solution | Summary |
|---|---|---|---|
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [Python3](leetcode/0020_Valid_Parentheses) | 開き括弧が同じ種類の括弧で閉じているか、開いている括弧は正しい順序で閉じているか判定する。 |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | [Python3](leetcode/0206_Reverse_Linked_List) | 与えられた連結リストを反転させたものを返す。 |

### Heap, Priority Queue

ヒープは優先度付きキューの実装の1つで、優先度付きキューは含まれる要素が何らかの優先度順に取り出されるという特徴を持っている。優先度付きキューは [heapq](https://docs.python.org/ja/3/library/heapq.html) として標準ライブラリに用意されている。後から要素が追加され、その度に最大 or 最小の要素を早く取り出したい場合に使われる。また、最大のk個の要素全てを求めるためには `heapq.nlargest` などを用いる。

要素の頻度については、標準ライブラリ `collections` にある [Counter](https://docs.python.org/ja/3/library/collections.html#collections.Counter) クラスを用いる。仕様は `dict` に近く、要素を辞書のキーとして保存し、そのカウントを辞書の値として保存する。

| # | Title | Solution | Summary |
|---|---|---|---|
| 703 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | [Python3](leetcode/0703_Kth_Largest_Element_in_a_Stream) | 整数 k とリスト nums で初期化され、整数 val をリストに追加しリストの k 番目の最大要素返す add メソッドを持ったクラスを実装する。 |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | [Python3](leetcode/0347_Top_K_Frequent_Elements) | 整数配列 nums と整数kが与えられたとき、最も頻度の高い k 個の要素を返せ。答えはどのような順番で返してもよい。 |
| 373 | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | [Python3](leetcode/0373_Find_K_Pairs_with_Smallest_Sums) | 昇順でソートされた2つの整数配列 nums1, nums2 から一つずつ要素を取り出し、和が最も小さい k 組のペア (u1, v1) を返す。 |

### HashMap

`Map` とは `Key` と `Value` を紐付けてデータを格納するデータ構造のことで、`Key` の重複が許されておらず、`Key` から `Value` を参照するような時に使われる。特定の `Key` が登録されているか1つずつ調べるのは効率的でないので、ハッシュテーブルを使った実装になっており、ハッシュ関数により特定の `Key` に対して出来るだけ一意の値を返すため、全てを調べる必要がなく効率的である。

汎用の `Python` 組み込みコンテナ `dict` の代わりに、[collections.defaultdict](https://docs.python.org/ja/3.10/library/collections.html) を使うこともできる。`defaultdict` では存在しない  `Key` が入ってもデフォルト値を生成することができるため、状況によってはコードを簡略化することができる。

重複をなくすだけであれば、`Python` には、[set](https://docs.python.org/ja/3/tutorial/datastructures.html#sets) (集合) を扱うためのデータ型がある。集合とは、重複する要素をもたない、順序づけられていない要素の集まりである。

| # | Title | Solution | Summary |
|---|---|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python3](leetcode/0001_Two_Sum) | 整数 nums の配列と整数 target が与えられたとき、2つの数値の和が target になるようなインデックスを返せ。 |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | [Python3](leetcode/0049_Group_Anagrams) | 文字列 strs の配列が与えられたとき、アナグラムをになっているものをグループ化して返す。 |
| 349 | [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | [Python3](leetcode/0349_Intersection_of_Two_Arrays) | 2つの整数配列 nums1, nums2 が与えられたとき、それらの共通している要素を返す。 |
| 929 | [Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/) | [Python3](leetcode/0929_Unique_Email_Addresses) | メールアドレスが複数入っている配列から、ユニークなメールアドレスの数をカウントして返す。 |
| 387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | [Python3](leetcode/0387_First_Unique_Character_in_a_String) | 文字列 s が与えられたとき、その中のユニークな文字の中ではじめに出て来るものを探し、そのインデックスを返す。もしそれが存在しなければ、-1 を返す。 |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | [Python3](leetcode/0560_Subarray_Sum_Equals_K) | 整数 nums の配列と整数 k が与えられたとき、その和が k に等しい部分配列の総数を返す。 |

### Graph, BFS, DFS

探索アルゴリズムでスタック（後に入れたものが先に出る）を使うかキュー（先に入れたものが先に出る）を使うかによって、深さ優先探索（スタック使用）か幅優先探索（キュー使用）になる。

`BFS`（幅優先探索）は、`Graph` の探索に用いられるアルゴリズムで、最小移動手数を求めるような出来るだけ根から近い部分を積極的に探索した方が効率が良いときに用いる。

`DFS`（深さ優先探索）は、`Graph` の探索に用いられるアルゴリズムで、スタートからゴールまで辿り着けるかを調べる問題のように、一度最後のノードまで探索した方が効率の良いときに用いる。

`DFS`（深さ優先探索）は再起を使って比較的簡単に書けるため、全て列挙する場合は`DFS`（深さ優先探索）を用いることが多い。最短路や最小手数などを求める場合は `BFS`（幅優先探索）の方が有効である。

| # | Title | Solution | Summary |
|---|---|---|---|
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | [Python3](leetcode/0200_Number_of_Islands) | 1（陸）と 0（水）の地図を表す m×n の2次元二項格子が与えられたとき、島の数を返す。 |
| 695 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | [Python3](leetcode/0695_Max_Area_of_Island) | 1（陸）と 0（水）の地図を表す m×n の2次元配列が与えられたとき、配列の中の島の最大面積を返す。島がない場合は 0 を返す。 |
| 323 | [🔒 Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [Python3](leetcode/0323_Number_of_Connected_Components_in_an_Undirected_Graph) | n 個のノードと無向のエッジのリストが与えられたとき、無向グラフの連結成分の数を求める関数を書け。 |
| 127 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | [Python3](leetcode/0127_Word_Ladder) | beginWord から endWord への最短で変換するのに必要な単語の数を返す。変換できるのは1文字違いの単語のみで、beginWord のみ wordList に存在する必要はない。 |

### Tree, BT, BST

`Binary Tree`（二分木）とは、データ構造の1つである。あるノードが持つ子の数が多くて2つであるものをいう。例えば、`Binary Search Tree`（二分探索）や `Heap`（ヒープ）を実装するために使われる。

`Binary Search Tree`（二分探索木）は、コンピュータプログラムにおいて、「左の値 ≤ 親の値 ≤ 右の値」という条件を持つ二分木である。

| # | Title | Solution | Summary |
|---|---|---|---|
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Python3](leetcode/0104_Maximum_Depth_of_Binary_Tree) | 二分木が与えられたとき、その最大深度を返す。 |
| 111 | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | [Python3](leetcode/0111_Minimum_Depth_of_Binary_Tree) | 二分木が与えられたとき、その最小の深さを求めよ。 |
| 617 | [Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/) | [Python3](leetcode/0617_Merge_Two_Binary_Trees) | 2本の二分木 root1 と root2 が与えられる。2本の二分木を重ね合わせた二分木を返す。 |
| 108 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | [Python3](leetcode/0108_Convert_Sorted_Array_to_Binary_Search_Tree) | 昇順にソートされた整数配列 nums が与えられたとき、それを高さバランスのとれた二分探索木に変換せよ。 |
| 112 | [Path Sum](https://leetcode.com/problems/path-sum/) | [Python3](leetcode/0112_Path_Sum) | 二分木のルートと整数の targetSum が与えられたとき、その木にルートから子を持たないノードへのパスがあり、そのパスに沿ったすべての値の合計が targetSum に等しい場合に真を返す。 |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Python3](leetcode/0102_Binary_Tree_Level_Order_Traversal) | 二分木のルートが与えられたとき、そのノードの深さごとに配列に分けて返す。 |
| 103 | [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | [Python3](leetcode/0103_Binary_Tree_Zigzag_Level_Order_Traversal) | 二分木のルートが与えられたとき、そのノードの値をジグザグ（右から左，左から右を交互に）にノードの深さ毎にまとめたものを返す。 |
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | [Python3](leetcode/0098_Validate_Binary_Search_Tree) | 二分木のルートが与えられたとき、それが有効な二分木探索木（BST）であるかどうかを判定しなさい。 |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [Python3](leetcode/0105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal) | 2つの整数配列 preorder と inorder が与えられ、preorder は前置走査、inorder は後置走査を表しており、これらをもとにして二分木を構築して返す。 |

### Sort

ソートアルゴリズムはいくつか種類があり、それぞれに特徴がある。基本的には、`安定ソートであるか`、`高速なソートであるか`、`実装が簡単であるか`、`元の並びに依存しないか`、`内部ソートであるか` に着目することでそれぞれの特徴を掴むことができる。

`挿入ソート (Insertion Sort)` は、次の要素を正しい位置に挿入していくことで端から徐々にソートしていく。安定ソートである。計算量オーダーは $Ο(n^2)$ で遅い。実装が簡単である。ほぼ整列済のデータに対して非常に高速である。内部ソートである。

`マージソート (Merge Sort)` は、配列を半分に分けて、それぞれをソートしておいて、その2つをマージすることを繰り返してソートしていく。安定ソートである。計算量オーダーは $O(n\log{n})$ で高速である。実装はそこまで複雑ではない。元の並びに依存しない。外部ソートである。

`クイックソート (QquickSort)` は、配列の中から適当な要素ピボットを選び出し、配列全体をピボット未満のグループとピボット以上のグループに分割することを繰り返してソートしていく。不安定ソートである。計算量オーダーは $Ο(n^2)$ であるが、偏りがない限り $O(n\log{n})$ で高速である。実装はやや複雑である。元の並びによって遅くなることがある。内部ソートである。

`ヒープソート (Heap Sort)` は、ソートではあまり使われないがヒープれ自体は重要なデータ構造である。ヒープに要素をすべてヒープに挿入して、最大値を順に取り出していくことでソートしたものを得る。不安定ソートである。計算量オーダーは $O(n\log{n})$ で高速である。実装はヒープがあれば簡単である。元の並びに依存しない。内部ソートである。

以上のソートアルゴリズムは「大小比較」を元にしているため、ソートする対象が数値、図形、文字列、など大小比較ができればよいという汎用性があった。実際には、速度重視のときは `クイックソート`、速度重視のときは `マージソート`、ほとんど並び替える必要がないときは `挿入ソート` が使われる。しかし、いずれも時間計算量 $O(n\log{n})$ がオーダーの限界であった。

しかしながら、 データの種類が整数であり、整数値の範囲が予め分かっていて、それほど大きくないという特殊な場合であればばあいであれば、時間計算量 $O(n)$ でソートが可能である。

`バケットソート (Bucket Sort)` は、あらかじめデータが取り得る全ての値の分だけバケツを順番どおりに並べて用意しておき、値を対応するバケツに入れてカウントし、後で取り出すことでソートを行う。`計数ソート (Counting Sort)` とも呼ばれる。基数（桁上がりの基準になる数）毎にバケットソートを行えるようにしたものが、`基数ソート (Radix Sort)` である。

使われないが、有名なソートアルゴリズムとして、`選択ソート (selection sort)` と `バブルソート (Bubble Sort)` がある。選択ソートは、残っているもののうち一番小さいものを前に持って来ることを繰り返す。バブルソートは、大きさが逆転している部分があったら交換することを繰り返す。どちらも計算量オーダーは $Ο(n^2)$ で遅く、バブルソートは最も遅いアルゴリズムの一つである。

> 参考資料:  
> [Toptal | Sorting Algorithms Animations](https://www.toptal.com/developers/sorting-algorithms)  
> [けんちょん | ソートを極める！ 〜 なぜソートを学ぶのか 〜](https://qiita.com/drken/items/44c60118ab3703f7727f)

### Dynamic Programming

`DP`（動的計画法）は、コンピュータで用いられるアルゴリズムの分類の1つである。イメージとしては、問題を小さな部分問題に分割し、それぞれの部分問題の計算結果を記録、同じ計算に対しては記録を参照することで省略するという流れになっている。

有名な例として「フィボナッチ数列」が取り上げられる。動的計画法を使わないず再帰で解いた場合は、$f(4) = f(3) + f(2)$ という計算をするために $f(3) = f(2) + f(1)$ が必要になるため、$f(2)$ の計算が重複してしまう。全く同じ計算を何度も何度も繰り返しているため効率が悪い。

そこで、`メモ化再帰` という方法が取られる。計算したことがなければ計算をして結果をメモし、計算したことがあれば計算結果を利用するという方法である。メモ化再帰をするためには、グローバル変数でメモを用意しておく必要がある。

| # | Title | Solution | Summary |
|---|---|---|---|
| 276 | [🔒 Paint Fence](https://leetcode.com/problems/paint-fence/) | [TODO](leetcode/0276_Paint_Fence) | --- |
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | [TODO](leetcode/0300_Longest_Increasing_Subsequence) | --- |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | [TODO](leetcode/0053_Maximum_Subarray) | --- |
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | [TODO](leetcode/0062_Unique_Paths) | --- |
| 63 | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | [TODO](leetcode/0063_Unique_Paths_II) | --- |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | [TODO](leetcode/0198_House_Robber) | --- |
| 213 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | [TODO](leetcode/0213_House_Robber_II) | --- |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [TODO](leetcode/0121_Best_Time_to_Buy_and_Sell_Stock) | --- |
| 122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | [TODO](leetcode/0122_Best_Time_to_Buy_and_Sell_Stock_II) | --- |
| 139 | [Word Break](https://leetcode.com/problems/word-break/) | [TODO](leetcode/0139_Word_Break) | --- |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | [TODO](leetcode/0322_Coin_Change) | --- |

### Binary Search

| # | Title | Solution | Summary |
|---|---|---|---|
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | [TODO](leetcode/0035_Search_Insert_Position) | --- |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [TODO](leetcode/0153_Find_Minimum_in_Rotated_Sorted_Array) | --- |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [TODO](leetcode/0033_Search_in_Rotated_Sorted_Array) | --- |
| 1011 | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | [TODO](leetcode/1011_Capacity_To_Ship_Packages_Within_D_Days) | --- |

### Recursion

| # | Title | Solution | Summary |
|---|---|---|---|
| 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | [TODO](leetcode/0050_Powx_n) | --- |
| 779 | [K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/) | [TODO](leetcode/0779_K-th_Symbol_in_Grammar) | --- |
| 776 | [🔒 Split BST](https://leetcode.com/problems/split-bst/) | [TODO](leetcode/0776_Split_BST) | --- |

### Sliding Window

| # | Title | Solution | Summary |
|---|---|---|---|
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [TODO](leetcode/0003_Longest_Substring_Without_Repeating_Characters) | --- |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | [TODO](leetcode/0209_Minimum_Size_Subarray_Sum) | --- |

### Greedy + Backtracking

| # | Title | Solution | Summary |
|---|---|---|---|
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | [TODO](leetcode/0046_Permutations) | --- |
| 78 | [Subsets](https://leetcode.com/problems/subsets/) | [TODO](leetcode/0078_Subsets) | --- |
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | [TODO](leetcode/0039_Combination_Sum) | --- |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | [TODO](leetcode/0022_Generate_arentheses) | --- |

### Practice

| # | Title | Solution | Summary |
|---|---|---|---|
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | [TODO](leetcode/0283_Move_Zeroes) | --- |
| 252 | [🔒 Meeting Rooms ](https://leetcode.com/problems/meeting-rooms/) | [TODO](leetcode/0252_Meeting_Rooms) | --- |
| 253 | [🔒 Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | [TODO](leetcode/0253_Meeting_Rooms_II) | --- |
| 392 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | [TODO](leetcode/0392_Is_Subsequence) | --- |
| 31 | [Next Permutation](https://leetcode.com/problems/next-permutation/) | [TODO](leetcode/0031_Next_Permutation) | --- |
| 8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | [TODO](leetcode/0008_String_to_Integer_atoi) | --- |
| 6 | [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion/) | [TODO](leetcode/0006_Zigzag_Conversion) | --- |

## Plan
自分自身の勉強のために解答をまとめているので、すべてを網羅するつもりはありません。  
リクエストやアドバイス、ご質問等ございましたら、お気軽にお問い合わせください。

## Reference
こちらの記事を参考にして問題を選択しています。  
[新井康平 | コーディング面接対策のために解きたいLeetCode 60問](https://1kohei1.com/leetcode/)

## Recommendation
他の解き方を見たい方には以下のレポジトリを見ることをおすすめします。  
[LeetCode in Go](https://github.com/halfrost/LeetCode-Go)  
[Python & JAVA Solutions for Leetcode (inspired by haoel's leetcode)](https://github.com/qiyuangong/leetcode)
