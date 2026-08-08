class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
     count_set={}
     len_cal=len(nums)//3
     for num in nums:
        if num in count_set:
            count_set[num]+=1
        else:
            count_set[num]=1
     freq=[]

     for key,value in count_set.items():
        if value>len_cal:
            freq.append(key)
     return freq
        
