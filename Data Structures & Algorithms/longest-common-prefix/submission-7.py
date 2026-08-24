class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        
        for word in strs[1:]:
            for i in range(min(len(prefix),len(word))):
                if prefix[i]!=word[i]:
                    prefix=prefix[0:i]
                    break
            else:
             prefix=prefix[0:min(len(prefix),len(word))]
            if prefix == " ":
                return " "
        return prefix
                
       