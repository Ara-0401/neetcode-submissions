class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        abs_diff=[]
       
        min_i=0

        for i in range(len(arr)):
            abs_diff.append(abs(arr[i]-x))

        min_sum=sum(abs_diff[0:k])
        
        curr_sum = min_sum
        for i in range(1,len(arr)-k+1):
            curr_sum=abs_diff[i+k-1]+curr_sum - abs_diff[i-1]

            if curr_sum < min_sum:
               min_sum = curr_sum
               min_i = i
        
        return arr[min_i:min_i+k]

        