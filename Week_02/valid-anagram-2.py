class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        counter = {}
        for i in range(len(s)):
            if s[i] not in counter:
                counter[s[i]] = 0
            if t[i] not in counter:
                counter[t[i]] = 1
            counter[s[i]] = counter[s[i]] + 1
            counter[t[i]] = counter[t[i]] - 1
        
        for num in counter.items():
            if num != 0:
                return False
        return True