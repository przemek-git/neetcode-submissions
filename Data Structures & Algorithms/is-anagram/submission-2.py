class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c_to_count1, c_to_count2 = {}, {}
        for c in s:
            c_to_count1[c] = 1 if c not in c_to_count1 else c_to_count1[c] + 1
        for c in t:
            c_to_count2[c] = 1 if c not in c_to_count2 else c_to_count2[c] + 1

        for c in c_to_count1:
            if c not in c_to_count2 or c_to_count2[c] != c_to_count1[c]:
                return False
        return True

