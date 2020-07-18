import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for temp_str in strs:
            sort_str = self.HashMapFunc(temp_str)
            if sort_str in result_dict:
                result_dict[sort_str].append(temp_str)
            else:
                result_dict[sort_str] = temp_str
        return list(result_dict.values())
    
    def HashMapFunc(self,temp_str):
        key = [0] * 26
        for char in temp_str:
            key[ord(char) - ord('a')] +=1
        return ''.join([str(i) for i in key])