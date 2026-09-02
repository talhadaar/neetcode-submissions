class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sort and return mid+1'th element O(nlog(n)) and no space
        # Hashmap: if element appears n/2 + 1 times, we found it O(N),O(N)

        # Attempt to pick a candidate from a pool of votes.
        # Candidate with most votes wins.
        # if a candidate gets out voted, pick the next one and repeat.
        # Candidate with most votes will survive.
        # This way we keep a running score of candidates
        # Candidate with more picks survives each time

        votes,candidate = 1,nums[0]
        for num in nums:
            if num==candidate:
                votes+=1
            else:
                votes-=1

            if votes == 0:
                candidate = num
                votes = 1
        return candidate