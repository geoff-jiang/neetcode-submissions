class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = defaultdict(int)
        for c in s1:
            counter[c] += 1

        def check(i, c):
            j = i + len(s1)
            if j > len(s2):
                return False
            for x in range(i, j):
                if c[s2[x]] <= 0:
                    return False
                c[s2[x]] -= 1
            return True
        
        for i in range(len(s2)):
            if s2[i] in counter:
                if check(i, counter.copy()):
                    return True
               
        return False

