class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_arr = sorted(nums1 + nums2)
        if len(merge_arr) % 2 != 0:
            return merge_arr[len(merge_arr)//2]
        else:
            return (merge_arr[len(merge_arr)//2] + merge_arr[len(merge_arr)//2 - 1])/2
