class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        def correspond(sym: str) -> str:
            match sym:
                case ')':
                    return '('
                case ']':
                    return '['

                case '}':
                    return '{'
                case _:
                    return None
        
        stack=[]
        for sym in s:
            if stack:
                if correspond(sym)==stack[-1]:
                    stack.pop()
                else:
                    stack.append(sym)
            else:
                stack.append(sym)
        if not(stack):
            return True
        return False
        