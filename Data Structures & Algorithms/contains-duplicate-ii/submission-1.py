class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Brute Force: Check every duplicate - nested loops for N size - Fixed window size
        # O(N*min(n,k)), O(1)

        # Use a hashmap, num->index
        # 1 iteration
        # If number was seen already, check difference in index of it's last occurance
        # if difference > k, update hashmap with latest
        # if difference <=k, return True
        # O(N), O(N)

        # Move window of size k, keep a set for recurring elements, reset set each iter
        # O(N), O(min(k,n))

        windowset = set()
        L = 0
        for R in range(len(nums)):
            if R-L > k:
                # remove first element of window, and slide up
                windowset.remove(nums[L])
                L+=1

            # check latest element found in window in set
            if nums[R] in windowset:
                return True
            # add latest to set
            windowset.add(nums[R])

        return False