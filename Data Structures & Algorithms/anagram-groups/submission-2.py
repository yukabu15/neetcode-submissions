class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagram = dict()

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in dict_anagram:
                dict_anagram[sorted_s].append(s)
            else:
                dict_anagram[sorted_s] = [s]
        
        ans = []
        for value in dict_anagram.values():
            ans.append(value)

        return ans