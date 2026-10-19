class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        freqArr = []
        for key, v in freq.items():   
            freqArr.append([-v, key])
        heapq.heapify(freqArr)
        res = []
        while k > 0:
            v, key = heapq.heappop(freqArr)
            res.append(key)
            k -= 1
        return res

        


