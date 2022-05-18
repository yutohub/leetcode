class Solution:
    def groupAnagrams(self, strs):
        def_dict = collections.defaultdict(list)
        for word in strs:
            chars = sorted(word) # list <- str
            sort_word = ''.join(chars) # str <- list
            def_dict[sort_word].append(word)
        return def_dict.values()
        