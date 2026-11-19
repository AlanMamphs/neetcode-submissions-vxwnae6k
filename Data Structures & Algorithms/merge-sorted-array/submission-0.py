class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                k = j
                while k + 1 < n and nums2[k] > nums2[k + 1]:
                    nums2[k], nums2[k + 1] = nums2[k + 1], nums2[k]
                    k += 1
            i += 1
        for j in range(n):
            nums1[i + j] = nums2[j]
        

                    
