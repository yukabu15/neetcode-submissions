class TimeMap:

    def __init__(self):
        self.time_map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.time_map.get(key):
            self.time_map[key] = []
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if self.time_map.get(key):
            cand = self.time_map[key]
            l, r = 0, len(cand)-1

            if cand[l][0] > timestamp:
                return ""

            while l <= r:
                m = l + (r - l) // 2
                if cand[m][0] <= timestamp:
                    l = m+1
                    ans = cand[m][1]
                else:
                    r = m-1
            
            return ans
        
        return ""

