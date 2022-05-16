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


## Plan

自分自身の勉強のために解答をまとめているので、すべてを網羅するつもりはありません。

リクエストやアドバイス、ご質問等ございましたら、お気軽にお問い合わせください。

## Reference

[新井康平 | コーディング面接対策のために解きたいLeetCode 60問](https://1kohei1.com/leetcode/)

## Recommendation

[LeetCode in Go](https://github.com/halfrost/LeetCode-Go)

[Python & JAVA Solutions for Leetcode (inspired by haoel's leetcode)](https://github.com/qiyuangong/leetcode)


