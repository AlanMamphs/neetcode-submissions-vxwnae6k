class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2

        l = 0
        r = len(A) - 1

        while True:
            a_l = l + (r - l) // 2
            a_r = a_l + 1
            b_l = half - a_l - 2
            b_r = b_l + 1

            ALeft = A[a_l] if a_l >= 0 else float('-inf')
            ARight = A[a_r] if a_r < len(A) else float('inf')
            BLeft = B[b_l] if b_l >= 0 else float('-inf')
            BRight = B[b_r] if b_r < len(B) else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2 == 1:
                    return min(ARight, BRight)
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            else:
                if ALeft > BRight:
                    r = a_l - 1
                else:
                    l = a_l + 1
        