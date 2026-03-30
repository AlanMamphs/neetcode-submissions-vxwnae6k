class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total // 2
        if len(A) > len(B):
            A, B = B, A
        
        l = 0
        r = len(A) - 1

        while True:
            m = l + (r - l) // 2
            b_m  = half - m - 2
            ALeft = A[m] if m >= 0 else float('-inf')
            BLeft = B[b_m] if (b_m) >= 0 else float('-inf')
            ARight = A[m+1] if m + 1 < len(A) else float('inf')
            BRight = B[b_m+1] if b_m + 1 < len(B) else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2 == 1:
                    return min(ARight, BRight)
                else:
                    return max(ALeft, BLeft) / 2 + min(ARight, BRight) / 2
            else:
                if ALeft > BRight:
                    r = m - 1
                else:
                    l = m + 1
            
