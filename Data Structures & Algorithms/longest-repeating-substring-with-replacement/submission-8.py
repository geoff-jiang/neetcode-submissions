class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = defaultdict(int)
        l = 0
        maxF = 0
        res = 0

        for r in range(len(s)):
            store[s[r]] += 1
            maxF = max(maxF, store[s[r]])

            while (r - l + 1) - maxF > k:
                store[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            
        return res