class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        
        # exception like Example 2
        if endWord not in wordList:
            return 0
        
        # dict to search neighborhood words
        neighbor = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbor[pattern].append(word)
                
        # shortest distance
        # 1. don't go to visited places
        visited = set([beginWord])
        # 2. using BFS
        que = collections.deque([beginWord])
        
        result = 1 # beginWord
        
        while que:
            for _ in range(len(que)):
                word = que.popleft()
                # conclusion
                if word == endWord:
                    return result
                # other case
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei_word in neighbor[pattern]:
                        if nei_word not in visited:
                            visited.add(nei_word)
                            que.append(nei_word)
            result += 1
        
        # if no such sequence exists
        return 0
