class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1

        print("da modulus: " + str(n%3))
        print("da division: ", str(n//3))
        threes = 3 ** (n // 3)
        if n % 3 == 1:
            print("da if return: ", str((threes//3)*4))
            return (threes//3)*4

        return threes * max(1, (n%3))