
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)

        for s in strs:
            charList = [0] * 26
            for c in s:
                charList[ord(c) - ord('a')] += 1
            dd[tuple(charList)].append(s)

        res = []
        for k in dd.values():
            res.append(k)
        return res
            

            



            

        