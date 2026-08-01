class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset={}
        freq_list=[]
        new_num=[]

        count=Counter(nums)
        for key,value in count.items():
            freq_list.append([value,key])
        freq_list.sort(reverse=True)
        
        for i in range(k):
            new_num.append(freq_list[i][1])
        return new_num

                 
