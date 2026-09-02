class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Subarray: Contigious bit of memory
        # Subarray sum must equal k
        # Input unsorted and negative numbers(sorting will break subarrays anyways)

        # Prefixes give us sub array sums prefix[j] - prefix[i] == k, then subarray i+1..j gives us a valid subarray
        # prefix[j]-k = prefix[i]
        # We test how many times we've seen prefix[i], each prefix[j]-prefix[i]=k will give us a valid subarray
        # so for every prefix[j] we find all valid prefix[j] seen so far.
        # so result will be summation of every prefix[j]-prefix[i] that had result k

        res=j=0
        psums = defaultdict(int)
        psums[0] = 1

        for num in nums:
            j+=num
            i = j-k

            if i in psums:
                res+=psums[i]
            psums[j]+=1
        return res