class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group_dict = dict()

        for string in strs:
            str_anagram = "".join(sorted(string))
            if str_anagram in anagram_group_dict:
                anagram_group_dict[str_anagram].append(string)
            else:
                anagram_group_dict[str_anagram] = [string]
            
        ans = []
        for string, group in anagram_group_dict.items():
            ans.append(group)

        return ans