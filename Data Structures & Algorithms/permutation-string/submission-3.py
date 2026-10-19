class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1chars, s2chars = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1chars[ord(s1[i]) - ord('a')] += 1
            s2chars[ord(s2[i]) - ord('a')] += 1
        
        matches = 0

        for i in range(26):
            if s1chars[i] == s2chars[i]:
                matches += 1
        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[i]) - ord('a')
            s2chars[index] += 1
            if s2chars[index] == s1chars[index]:
                matches += 1
            elif s2chars[index] - 1 == s1chars[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2chars[index] -= 1
            if s2chars[index] == s1chars[index]:
                matches += 1
            elif s2chars[index] + 1 == s1chars[index]:
                matches -= 1
            l += 1
            print(matches)
        
        return matches == 26
                

            