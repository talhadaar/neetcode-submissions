class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sort and return mid+1'th element O(nlog(n)) and no space
        # Hashmap: if element appears n/2 + 1 times, we found it O(N),O(N)

        # Attempt to pick a candidate from a pool of votes.
        # Candidate with most votes wins.
        # if a candidate gets out voted, pick the next one and repeat.
        # Candidate with most votes will survive.
        # This way we keep a running score of candidates
        # where scores cancel each other out, until candidate with maximum score is left
        # Candidate with more picks survives each time

        # Alternatively: Probability of picking majority candidate is >50%
        # Randomly pick candidates, if one is picked 6 out of 10 tries, that is the majority one
        count = candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate