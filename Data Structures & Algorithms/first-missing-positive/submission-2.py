class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n=len(nums)
        

        freq_dict=[0] *(n+1)

        for num in nums:
            if 0 < num <= n :
                freq_dict[num] +=1

        sorted_nums = {}

        for i in range(len(freq_dict)):
            if freq_dict [i] > 0 :
                sorted_nums[i] = freq_dict[i]

        values=[]
        for key,value in sorted_nums.items():
            values.append(key)
        if not values:
            return 1 

        max_val=max(values)
       
        for i in range(1,max_val):
            if i not in values :
               return i
        return max_val + 1
        



