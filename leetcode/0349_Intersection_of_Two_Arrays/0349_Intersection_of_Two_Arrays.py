class Solution:
    def intersection(self, nums1, nums2):
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        common = nums1_set & nums2_set
        return common
        