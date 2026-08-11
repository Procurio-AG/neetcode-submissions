class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map={}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in target_map:
                return [target_map[diff],i]
            target_map[nums[i]] = i
        return None
            
                

            
            
        