class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        A = nums1
        B = nums2

        total = len(A) + len(B)

        # Binary search the smaller array
        if len(A) > len(B):
            A, B = B, A

        half = total // 2

        # i is the index of the last element on A's left side
        l = -1
        r = len(A) - 1

        while l <= r:
            i = (l + r) // 2
            j = half - i - 2

            A_l = A[i] if i >= 0 else float("-inf")
            A_r = A[i + 1] if i + 1 < len(A) else float("inf")

            B_l = B[j] if j >= 0 else float("-inf")
            B_r = B[j + 1] if j + 1 < len(B) else float("inf")

            if A_l <= B_r and B_l <= A_r:
                if total % 2 == 1:
                    return min(A_r, B_r)

                return (max(A_l, B_l) + min(A_r, B_r)) / 2

            if A_l > B_r:
                # Move the partition in A left
                r = i - 1
            else:
                # Move the partition in A right
                l = i + 1

        raise ValueError("Input arrays are not sorted")