class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      dict_s={}
      for char in s:
        if char in dict_s:
            dict_s[char]+=1
        else:
            dict_s[char]=1
      if len(s)!=len(t):
        return False
   
      for char in t:
        if not char in dict_s or dict_s[char]==0:
            return False
        dict_s[char]-=1
      return True


       
