class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        r=len(nums)
        if r<=1:
            return r
        max_len=0
        i=0
        num_set=set(nums)
        while i<r:
            l=1
            c=nums[i]
            if ((c-1) in num_set):
                i+=1
                continue
            while (c+1 in num_set):
                c+=1
                l+=1
            max_len=max(max_len,l)
            i+=1
        
        return max_len       