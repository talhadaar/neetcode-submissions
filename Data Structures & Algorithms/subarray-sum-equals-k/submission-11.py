class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Subarray,substring=potato,potato
        # Brute Force: Make all subarrays, check subs and count valid ones
        # O(N^2)

        # 2 Pointer: Cannot guarantee if moving a point increases/decreases the sum
        # prefix[j]-k==prefix[i]

        fmap = defaultdict(int)
        fmap[0]=1

        j = 0
        res = 0

        for num in nums:
            j = j+num

            i = j - k
            res += fmap[i]
            fmap[j]+=1
        return res