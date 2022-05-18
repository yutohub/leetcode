class Solution:
    def twoSum(self, nums, target):
        pair = {}
        for i, n in enumerate(nums):
            pair[target - n] = i
        for i, n in enumerate(nums):
            if n in pair and i != pair[n]:
                return [i, pair[n]]
                