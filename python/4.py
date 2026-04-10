class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums = nums1 + nums2
        nums.sort()
        longitud = len(nums)
        mitad = int(longitud//2)
        
        if longitud % 2 == 0:
            return float((nums[mitad-1] + nums[mitad])/2)
        else:
            return float(nums[mitad])

