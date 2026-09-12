class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=[]
        for i in s:
            if i.isalnum():
                temp.append(i.lower())
        l,r=0,len(temp)-1
        while(l<r):
            if temp[l]!=temp[r]:
                return False
            l+=1
            r-=1

        return True