class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        r=len(nums)
        max_len=0
        i=0
        num_d={x:0 for x in nums}
        while i<r:
            l=1
            c=nums[i]
            if num_d[c]==1 or ((c-1) in num_d):
                i+=1
                continue
            num_d[c]=1
            while (c+1 in num_d):
                c+=1
                l+=1
                num_d[c]=1
            max_len=max(max_len,l)
            i+=1
        
        return max_len



        