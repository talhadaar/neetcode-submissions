class Solution:
    def isValid(self, s: str) -> bool:
        closing = {')':'(', '}':'{',']':'['}
        stk = []

        for brac in s:
            if brac in closing:
                if not stk or stk[-1]!=closing[brac]:
                    return False
                stk.pop()
            else:
                stk.append(brac)

        return len(stk)==0
