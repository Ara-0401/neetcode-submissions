class Solution:
    def daysNeeded( self ,weights,capacity):
        day = 1
        load = 0

        for w in weights:
            if load + w > capacity:
                day+=1
                load = w
            else:
                load+=w
        return day

    def shipWithinDays(self, weights: List[int], days: int) -> int:

      low ,high = max(weights), sum(weights)

      while low < high:
        mid = (low + high)//2

        if self.daysNeeded(weights,mid)<=days:
            high = mid
        else:
            low = mid+1
      return low
  