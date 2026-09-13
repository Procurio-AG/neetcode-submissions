class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        max_len=0
        l,r=0,0
        seen=set()
        for r in range(n):
            if s[r] in seen:
                while l<r and (s[r] in seen):
                    seen.remove(s[l])
                    l+=1
            seen.add(s[r])
            max_len=max(max_len,r-l+1)        
            
        return max_len
            