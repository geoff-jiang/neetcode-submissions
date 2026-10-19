class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)
        counter2 = defaultdict(int)
        for c in s:
            counter[c] += 1
        
        for c in t:
            counter2[c] += 1
        
        return counter == counter2