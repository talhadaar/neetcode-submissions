class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return ALL the triplets that sum to 0
        # i,j,k will be distinct, (cannot pick an idx more than once)
        # cannot return duplicate triplets

        nums.sort()
        n = len(nums)
        res = []

        for idx,num in enumerate(nums):

            # if all remaining numbers are non descending positives, we cannot sum to 0            
            if num > 0:
                break

            # skip duplicate
            if idx>0 and num==nums[idx-1]:
                continue

            l,r = idx+1, n-1
            while l<r:
                tsum = num + nums[l] + nums[r]
                if tsum>0:
                    r-=1
                elif tsum<0:
                    l+=1
                else:
                    res.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1
                    # move up to ignore dupes
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res