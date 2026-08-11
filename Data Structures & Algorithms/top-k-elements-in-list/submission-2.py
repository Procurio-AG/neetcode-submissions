class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums).most_common(k)
        res=[]
        for _ in d:
            res.append(_[0])
        return res

            
        