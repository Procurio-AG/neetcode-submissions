class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)   
        max_len=0

        for num in num_set:
            if num-1 in num_set:
                continue
            cur=num
            streak=1
            while cur+1 in num_set:
                cur+=1
                streak+=1
            max_len=max(max_len,streak)

        return max_len
            