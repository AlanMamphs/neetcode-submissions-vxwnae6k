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
            i = l + (r - l) // 2
            j = half - i - 2

            a_left = A[i] if i >= 0 else float('-inf')
            a_right = A[i + 1] if i + 1 < len(A) else float('inf')
            b_left = B[j] if j >= 0 else float('-inf')
            b_right = B[j + 1] if j + 1 < len(B) else float('inf')

            if a_left <= b_right and b_left <= a_right:
                # found correct positions
                if total % 2 == 1:
                    return min(a_right, b_right)
                else:
                    return max(a_left, b_left) / 2 + min(a_right, b_right) / 2
            else:
                if a_left > b_right:
                    r = i - 1
                else:
                    l = i + 1
