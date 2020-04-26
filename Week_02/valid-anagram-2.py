class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        sList = s.split('')
        tList = t.split('')
        counter = {}
        for i in range(len(s)):
            counter[sList[i]] += counter[sList[i]]
            counter[tList[i]] -= counter[tList[i]]
        
        for key, num in counter:
            if num != 0:
                return False;
        return True