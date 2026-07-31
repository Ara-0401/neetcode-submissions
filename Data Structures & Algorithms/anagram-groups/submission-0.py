class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_str={}
        new_strs=[]
        for item in strs:
            sorted_item="".join(sorted(item))
            if sorted_item in new_str:
                new_str[sorted_item].append(item)
            else:
                new_str[sorted_item]=[item]
        for key,val in new_str.items():
            new_strs.append(val)
        return new_strs
            