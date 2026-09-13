class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        n=len(nums)
        res=[]
        i=0
        while(i<n):
            n1=nums[i]
            tg=-n1
            l,r=i+1,n-1
            while l<r:
                s=nums[l]+nums[r]
                if s<tg:
                    l+=1
                elif s>tg:
                    r-=1
                else:
                    res.append([n1,nums[l],nums[r]])
                    r-=1
                    while l<r and nums[l]==nums[l-1]: l+=1
                    while l<r and nums[r]==nums[r+1]: r-=1
            while i<n and (nums[i]==n1):
                i+=1
        return res


            
