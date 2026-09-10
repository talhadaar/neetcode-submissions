class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        n = len(s)

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        def backtrack(i):
            if i == n:
                res.append(part.copy())
                return

            for j in range(i, n):
                if isPalindrome(i, j):
                    part.append(s[i:j+1])
                    backtrack(j + 1)
                    part.pop()

        backtrack(0)
        return res