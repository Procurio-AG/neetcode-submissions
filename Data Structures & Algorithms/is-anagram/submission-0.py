class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count_map(s):
            di={}
            for i in s:
                di[i] = di.get(i,0)+1
            return di
        return count_map(s)==count_map(t)