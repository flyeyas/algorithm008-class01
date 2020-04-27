class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        dic1 = [0]*26
        for i in range(len(s)):
            dic1[ord(s[i])-ord('a')] += 1
            dic1[ord(t[i])-ord('a')] -= 1
        for num in dic1:
            if num != 0:
                return False
        return True