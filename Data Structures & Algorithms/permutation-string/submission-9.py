class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:                                                                        
            return False
        need, window = [0] * 26, [0] * 26
        for i in range(m):
            need[ord(s1[i]) - 97] += 1
            window[ord(s2[i]) - 97] += 1

        for r in range(m, n):
            if need == window:
                return True
            window[ord(s2[r]) - 97] += 1
            window[ord(s2[r - m]) - 97] -= 1
        return need == window