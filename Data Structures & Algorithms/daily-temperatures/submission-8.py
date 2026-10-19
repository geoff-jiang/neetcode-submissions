class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        arr = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1):
            temp = i + 1
            while temperatures[temp] <= temperatures[i]:
                if arr[temp] == 0:
                    break
                temp += arr[temp]
            
            if temperatures[temp] > temperatures[i]:
                arr[i] = temp - i
        
        return arr


            