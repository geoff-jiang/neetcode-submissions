class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # start with empty list
        # copy all entries and append each element to each entry! 

        res = [[]]
        for n in nums:
            temp = [subset + [n] for subset in res]
            res += temp
        return res
