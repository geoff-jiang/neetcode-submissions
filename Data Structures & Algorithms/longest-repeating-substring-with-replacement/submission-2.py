class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqSet = defaultdict(int)
        maxFreq = 0
        res = 0
        l = 0
        for r in range(len(s)):
            freqSet[s[r]] += 1
            maxFreq = max(maxFreq, freqSet[s[r]])
            while r - l + 1 - maxFreq > k: 
                freqSet[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
