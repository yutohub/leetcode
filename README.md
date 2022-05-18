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

## Plan

自分自身の勉強のために解答をまとめているので、すべてを網羅するつもりはありません。

リクエストやアドバイス、ご質問等ございましたら、お気軽にお問い合わせください。

## Reference

[新井康平 | コーディング面接対策のために解きたいLeetCode 60問](https://1kohei1.com/leetcode/)

## Recommendation

[LeetCode in Go](https://github.com/halfrost/LeetCode-Go)

[Python & JAVA Solutions for Leetcode (inspired by haoel's leetcode)](https://github.com/qiyuangong/leetcode)


