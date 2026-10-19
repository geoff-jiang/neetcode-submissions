class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        1, 2, 3, 4, 5,    1
        median = 112345 2 + 3 / 2 = 2.5

        binary search on both arrays, compare middles? 
        1234. 5678. 

        binary search on both arrays, split them in the middle
        max of the left half should always contian numbers 
        smaller than the minimum in right half.

        aim to find the median since left half of both arrays
        added together should be exactly = m + n / 2


        """
        total = len(nums1) + len(nums2)
        half = total // 2

        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            mA = l + (r - l) // 2
            mB = half - mA - 2 
            leftA = A[mA] if mA >= 0 else float("-infinity")
            rightA = A[mA + 1] if mA + 1 < len(A) else float("infinity")
            leftB = B[mB] if mB >= 0 else float("-infinity")
            rightB = B[mB + 1] if mB + 1< len(B) else float("infinity")

            if leftA <= rightB and leftB <= rightA:
                # good partition
                if total % 2: 
                    return min(rightA, rightB)
                return float(max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                r = mA - 1
            else:
                l = mA + 1
            


