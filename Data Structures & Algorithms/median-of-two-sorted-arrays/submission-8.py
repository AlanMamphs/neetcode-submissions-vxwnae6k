class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        l = -1
        r = len(A) - 1

        while l <= r:
            a = (l + r) // 2
            b = half - a - 2

            AL = A[a] if a >= 0 else float('-inf')
            AR = A[a + 1] if a + 1 < len(A) else float('inf')
            BL = B[b] if b >= 0 else float('-inf')
            BR = B[b + 1] if b + 1 < len(B) else float('inf')

            if AL <= BR and BL <= AR:
                if total % 2:
                    return min(AR, BR)
                return (max(AL, BL) + min(AR, BR)) / 2
            
            if AL > BR:
                r = a - 1
            else:
                l = a + 1

