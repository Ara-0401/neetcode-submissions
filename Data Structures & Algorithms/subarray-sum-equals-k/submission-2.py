class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = { 0 : 1}
        runningSum = 0
        count = 0

        for i in range( len(nums)):
            runningSum += nums[i]
            
            check = runningSum - k

            if check in prefixMap:
                count += prefixMap[check]

            prefixMap[runningSum] = prefixMap.get(runningSum, 0) +1
        return count 
     


