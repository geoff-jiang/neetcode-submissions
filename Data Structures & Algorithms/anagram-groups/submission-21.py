class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lib = defaultdict(list)

        res = []

        for s in strs:
            key = [0] * 26
            for c in s: 
                key[ord(c) - 97] += 1
            lib[tuple(key)].append(s)
        
        for _, v in lib.items():
            res.append(v)
        
        return res
           



