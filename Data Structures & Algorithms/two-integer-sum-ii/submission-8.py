class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # numbers seen so far at i'th index
        # If the complement of current number was  already seen, then we return the 1 indexed pair
        mp = defaultdict(int)
        for idx,num in enumerate(numbers):
            complement = target - num
            if complement in mp:
                return [mp[complement]+1, idx+1]
            mp[num] = idx
        return []