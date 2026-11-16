class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # go through string
        # at each letter, either replace with previous if different, or start new streak? 
        # if replace w previous, recursion with k - 1? 

        # sliding window: maintain a window where the diff between chars is at most k. 
        # if greater, shrink window from the left? 
        # AABBCC k = 2 use a set to keep track of what characters are in the window? 
        # keep track of most frequent char? 
        # hash map to keep  track?
        # shrink the window until...?
        

        freq = defaultdict(int)
        res = 0
        l = 0
        max_freq = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            while (r - l + 1 - max_freq) > k:
                freq[s[l]] -= 1 
                l += 1

            res = max(res, r - l + 1)

        
        return res