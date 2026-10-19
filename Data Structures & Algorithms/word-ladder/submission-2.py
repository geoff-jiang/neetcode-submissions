class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        words, res = set(wordList), 0
        q = deque([beginWord])
        while q:
            res += 1
            for i in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return res
                for i in range(len(curr)):
                    for c in range(97, 123):
                        if chr(c) == curr[i]:
                            continue
                        temp = curr[:i] + chr(c) + curr[i + 1:]
                        if temp in words:
                            q.append(temp)
                            words.remove(temp)
        return 0
        
