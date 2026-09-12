class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)
        pre=[1]*r
        post=[1]*r
        c=0
        while (c<r):
            if c==0:
                pre[c]=1
            else:
                pre[c]=pre[c-1]*nums[c-1]
            c+=1
        c-=1
        while (c>=0):
            if c==r-1:
                post[c]=1
            else:
                post[c] = post[c+1]*nums[c+1]
            c-=1
        
        res=[]
        for i in range(r):
            res.append(pre[i]*post[i])
        return res

        
        