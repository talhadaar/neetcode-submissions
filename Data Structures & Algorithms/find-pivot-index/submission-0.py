class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Make prefix array
        # find a num[M] where prefix[0..M-0] == prefix[M+1..N]

        # Prefix array and binary search O(nLog(n))
# [0,1,2, 3, 4, 5, 6] 
# [1,7,3, 6, 5, 6,  ]
# [0,1,8,11,17,22,28]

        # prefix[i] == Prefix sum upto and including i'th number
        # nums[i] can be negative, nor prefix[] is not guaranteed to be monotonic
        total = 0
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i]+nums[i]

        
        for i in range(n):
            lhss = prefix[i]
            rhss = prefix[-1] - prefix[i+1]
            if lhss == rhss:
                return i
        return -1