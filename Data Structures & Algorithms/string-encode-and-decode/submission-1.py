class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        idx = 0
        ans = []
        while idx < len(s):
            end_idx = idx
            while s[end_idx] != "#":
                end_idx += 1
            len_string = int(s[idx:end_idx])
            ans.append(s[end_idx+1:end_idx+len_string+1])
            idx = end_idx+len_string+1

        return ans