class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output[i]: product of array except the nums[i] value
        # Brute force: pick a number, * the rest, create output
        # O(N*N), O(N)

        # Calculate product of array, and output[i] = prod(nums)//nums[i]
        # O(2N),O(N)

        # Interesting bit: If theres 1 zero in array: theres 1 non zero in output, rest are 0, if there's more than 1 zero, everything is 0

        n = len(nums)
        # calc the prod
        zeros = 0
        tp = 1
        for num in nums:
            if num == 0:
                zeros+=1
                # return if more than 1 zero
                if zeros > 1:
                    return [0]*n
                continue
            tp = tp * num

        res = [0] * n
        for i in range(n):
            if not zeros:
                res[i] = tp//nums[i]
            else:
                if nums[i]==0:
                    res[i] = tp

        return res