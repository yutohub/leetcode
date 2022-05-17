class Solution(object):
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        # keyにgetメソッドを渡してあげている
        return heapq.nlargest(k, counter.keys(), key=counter.get)