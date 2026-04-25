class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        bracket_pair = {"}":"{", "]":"[", ")":"("}

        for i in range(len(s)):
            if s[i] in bracket_pair.values():
                if i == len(s) - 1:
                    return False
                q.append(s[i])
            else:
                if q:
                    last = q.pop()
                    if bracket_pair[s[i]] != last:
                        return False
                else:
                    return False
        
        if q:
            return False
        else:
            return True