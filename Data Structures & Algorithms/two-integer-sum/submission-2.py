class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
           seen={}
           for i, num in enumerate(nums):
             comple=target-num
             if comple in seen:
                return [seen[comple],i]
             else:
                 seen[num]=i
           return []