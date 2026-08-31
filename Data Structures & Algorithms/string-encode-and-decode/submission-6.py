class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for i in strs:
            res.append(str(len(i)))
            res.append('#')
            res.append(i)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res=[]
        i,j=0,0
        l=len(s)
        while(i<l):
            j=i
            while(s[j]!='#' and j<l):
                j+=1
            length=int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res
        