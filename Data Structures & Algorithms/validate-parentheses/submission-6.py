class Solution:
    def isValid(self, s: str) -> bool:
        closing = {')':'(', ']':'[','}':'{'}
        stk = []

        for c in s:
            # if stk and closing[c]==stk[-1]:
            #     stk.pop()
            if c in closing and stk:
                # If we have a closing bracket
                # and top of stack is it's closing bracket
                # we pop it
                if stk[-1] == closing[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)

        # if stack has emptied, the string is valid
        # else invalid
        return True if not stk else False