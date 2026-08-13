class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 !=0:
            return False

        closedBy = {'(':')', '{':'}', '[':']'}
        opens = closedBy.keys()

        stk = []
        for i in range(len(s)):
            print("si: " + s[i])
            if s[i] in opens:
                stk.append(s[i])
                print('STACK: ' + str(stk))
            else:
                if not stk or s[i] != closedBy[stk[-1]]:
                    return False    
                stk.pop()

        if len(stk) == 0:
            return True

        return False