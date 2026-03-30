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
            a_m = l + (r - l) // 2
            b_m = half - 1 - (a_m + 1)
            a_left = A[a_m] if a_m >= 0 else float('-inf')
            b_left = B[b_m] if b_m >= 0 else float('-inf')
            a_right = A[a_m + 1] if a_m + 1 < len(A) else float('inf')
            b_right = B[b_m + 1] if b_m + 1 < len(B) else float('inf')

            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 1:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            else:
                if a_left > b_right:
                    r = a_m - 1
                else:
                    l = a_m + 1
        