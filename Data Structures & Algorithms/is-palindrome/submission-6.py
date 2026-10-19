import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        for i in range(len(clean)//2):
            n = len(clean) - 1 - i
            print(clean[i])
            print(clean[n])
            if (clean[i] != clean[n]):
                return False
        return True

