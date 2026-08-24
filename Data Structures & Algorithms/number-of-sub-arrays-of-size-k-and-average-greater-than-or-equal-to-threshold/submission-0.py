class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Brute: Find all subarrays of size k, check averages, count valid ones
        # O(N*k), O(1)

        # Run window of fixed size, get their sum, and do sum/2, if valid the count
        # Build a window of size k and it's sum
        # if window size exceedes, move up and remove it's earliest(L'th) element from sum
        # add latest element to sum and repeat

        count = 0 # valid subarrays of k size
        L = 0 # Earliest element of the window
        currSum = 0 # running sum of current window

        for R in range(len(arr)):
            # window size excedded
            currSum+=arr[R]

            if R-L+1 ==  k:
                # check avg
                if currSum / k >=threshold:
                    count+=1

                currSum -=arr[L]
                L+=1

        return count