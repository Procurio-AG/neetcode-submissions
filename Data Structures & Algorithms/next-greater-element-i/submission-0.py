class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        max_st=[nums2[-1],]
        n=len(nums2)-2
        res={nums2[n+1]:-1}
        while (n>=0):
            while max_st and nums2[n]>max_st[-1]:
                max_st.pop()
            
            if (max_st):
                res[nums2[n]]=max_st[-1]
            else:
                res[nums2[n]]=-1

            max_st.append(nums2[n])

            n-=1

        result=[]
        for i in nums1:
            result.append(res[i])
        return result

        