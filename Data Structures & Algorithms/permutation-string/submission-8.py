class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2 contains permutation of s1?
        # O(M*N),O(1): Hashmap freq count of chars in s2, iterate s1 and count against s2's hashmap


        # Slide a fixed size window over s2
        # check that char frequences of the the window match s1's

        m=len(s1)
        n=len(s2)

        if m>n:
            return False

        # s1 char counts
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(m):
            s1_count[ord(s1[i]) - ord('a')] += 1
            # first window of size m
            s2_count[ord(s2[i]) - ord('a')] += 1

        # count matches in first window
        matches = 0
        for i in range(26):
            matches+=(1 if s1_count[i] == s2_count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # move r ptr right
            idx = ord(s2[r]) - ord('a')
            s2_count[idx]+=1
            if s1_count[idx] == s2_count[idx]:
                matches +=1
            elif s1_count[idx]+1 == s2_count[idx]:
                matches -=1

            # move l ptr right
            idx = ord(s2[l]) - ord('a')
            s2_count[idx] -=1
            if s2_count[idx] == s1_count[idx]:
                matches+=1
            elif s1_count[idx] - 1 == s2_count[idx]:
                matches -=1
            l+=1
        return matches == 26