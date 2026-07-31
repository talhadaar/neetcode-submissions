class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1

        threesProd = 3 ** (n // 3) # 3^(n/3)
        print("threesProd: " + str(threesProd))
        if n % 3 == 1:
            # take the last ...*3*1
            # replace it with 2*2 to maximize

            # remove a 3 and mult 2*2=4
            return (threesProd//3)*4

        # handle remainder 0 or 2(cannot maximize two)
        return threesProd * max(1, (n%3))