class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0
        dq = deque([0])
        
        seen = set({0})

        if amount == 0: return 0

        while dq:
            res += 1
            for i in range(len(dq)):
                # grab first value from queue
                val = dq.popleft()
                for c in coins:
                    temp = val + c
                    if temp == amount:
                        return res
                    elif temp > amount or temp in seen:
                        continue
                    dq.append(temp)
                    seen.add(temp)
               
        return -1
                
