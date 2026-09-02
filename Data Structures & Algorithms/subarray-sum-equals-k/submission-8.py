class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Subarray: Contigious bit of memory
        # Subarray sum must equal k
        # Input unsorted and negative numbers(sorting will break subarrays anyways)

        # Brute Force: Making all subarrays and count whomst sum equals k
        # Start at i, make sub arrays of lenght upto n, keep checking sum
        # O(N*N)
        # Variable Window concept(window size increases till n, then window start is moved up)

        # 2 pointers: but when to reduce or expand which over the range predictably?

        # Prefixes give us sub array sums prefix[j] - prefix[i] == k, then subarray i+1..j gives us a valid subarray
        # prefix[j]-k = prefix[i]
        # If prefix[i] was already seen, we have another valid subarray
        # so for every prefix[j] we count how many previous valid subarays we've already seen
        
        prefixSums = defaultdict(int)
        prefixSums[0] = 1
        res=j=0

        for num in nums:
            j+=num
            i = j-k

            res+=prefixSums[i]
            prefixSums[j]+=1
        return res