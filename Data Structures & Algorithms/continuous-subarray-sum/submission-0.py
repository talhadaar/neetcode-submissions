class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #(prefix[i]-prefix[j]) % k = 0
        # prefix[j]%k - prefix[i]%k = 0
        # is same remainder repeats for 2 subarrays, and their length is >=2, we have a result

        remmap = {0:-1}

        total = 0
        for i,num in enumerate(nums):
            total+=num
            rem = total%k
            if rem not in remmap:
                remmap[rem] = i
            elif i-remmap[rem]>1:
                return True
        return False
