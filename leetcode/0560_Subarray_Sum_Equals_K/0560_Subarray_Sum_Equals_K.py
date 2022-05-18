class Solution:
    def subarraySum(self, nums, k):
        counter = 0
        left_sum = 0
        seen = {0: 1}
        for n in nums:
            left_sum += n
            diff = left_sum - k
            counter += seen.get(diff, 0)
            seen[left_sum] = seen.get(left_sum, 0) + 1
        return counter
