class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_count={}
        for num in nums:
            if num in duplicate_count:
               duplicate_count[num]+=1
            else:
                duplicate_count[num]=1
        for key,value in duplicate_count.items():
            if value>=2:
                return True
        return False


        