class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        n=len(nums)
        res=set()
        for i in range(n):
            seen=set()
            for j in range(i+1,n):
                n2,n1=nums[i],nums[j]
                tg=-(n1+n2)
                if tg in seen:
                    res.add((n1,n2,tg))
                seen.add(nums[j])
        result=[]
        for i in res:
            j=list(i)
            result.append(j)
        return result



            
