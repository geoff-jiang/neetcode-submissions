class TimeMap:

    def __init__(self):
        self.store = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = self.store[key]
        val[timestamp] = value
        self.store[key] = val


    def get(self, key: str, timestamp: int) -> str:
        if self.store[key] == {}:
            return ""
        val = self.store[key]
        valArray = list(val)
        l, r = 0, len(valArray) - 1
        while l <= r: 
            m = math.ceil(l + (r - l) / 2)
            if valArray[m] == timestamp:
                return val[valArray[m]]
            elif valArray[m] < timestamp:
                l = m + 1
            else:
                r = m - 1
        return val[valArray[r]] if valArray[r] <= timestamp else ""
