class Solution:
    def numDecodings(self, s: str) -> int:
        
        # #dp array from reverse
        # # store number of valid decoddings from s[i:]
        # dp = {len(s): 1}

        # # loop backwards
        # # if a character is non zero, dp[i] = dp[i + 1]
        # # if 1 or 2, and next digit is valid, + dp[i + 2]

        # for i in range(len(s) - 1, -1, -1):
        #     if s[i] == "0":
        #         dp[i] = 0
        #     else:
        #         dp[i] = dp[i + 1]
        #     if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
        #         dp[i] += dp[i + 2]
        
        # return dp[0]


        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1


        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
                if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                    dp[i] += dp[i + 2]
            
        return dp[0]












