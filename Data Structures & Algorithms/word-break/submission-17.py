class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Top Down -> what do i need to get there

        memo = {len(s): True}
        # last index = "" = True can be split
        words = set(wordDict)

        def dfs(i):
            if i in memo:
                return memo[i]
        
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    if dfs(i+len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        
        return dfs(0)