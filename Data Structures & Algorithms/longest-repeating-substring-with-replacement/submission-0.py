class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      count={}
      left , res =0 , 0

      for r in range(len(s)):
        count[s[r]]=1+count.get(s[r],0)
        if (r-left+1) - max(count.values()) > k:
            count[s[left]]-=1
            left+=1
        res = max(res,r-left+1)

      return res


        