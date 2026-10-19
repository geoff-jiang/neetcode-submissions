class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        v = defaultdict(int)
        # num: count
        for n in nums: 
            v[n] += 1
        count = list(v.values())
        count.sort(reverse = True)
        # count is a array of the most common occurences
        # search v for the values that match the first k items
        res = []
        for i in range(k):
            for key, value in v.items():
                if value == count[i] and key not in res:
                    res.append(key)
                    if len(res) == k:
                        return res
            #append the first 2 keys to res
        return res


