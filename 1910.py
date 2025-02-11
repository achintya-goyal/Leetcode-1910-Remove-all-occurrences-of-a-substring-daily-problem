class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        j = 0
        i = len(part)
        while i<=len(s):
            if s[j:i]==part:
                s = s[:j] + s[i:]
                j = -1
                i = len(part) - 1
            j+=1
            i+=1
        return s
