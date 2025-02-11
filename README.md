# Leetcode-1910-Remove-all-occurrences-of-a-substring-daily-problem

Problem Statement:

Given a string s and a string part, remove all occurrences of part from s one at a time until no more occurrences are left. The order of characters should remain the same.

Solution Explanation:

This solution iteratively scans the string s to find occurrences of the substring part. When an occurrence is found, it is removed, and the scanning restarts to ensure all occurrences are deleted.

Approach:

Initialize two pointers:

j: Marks the start of the scanning window.

i: Marks the end of the scanning window, initially set to the length of part.

Use a while loop to iterate through s while i is within bounds.

If a substring match (s[j:i] == part) is found:

Remove the substring from s.

Reset j to -1 and i to len(part) - 1 to restart the scan.

Increment both j and i after each iteration to slide the window forward.

Return the modified string after all occurrences are removed.

Code Implementation:

class Solution:

    def removeOccurrences(self, s: str, part: str) -> str:
    
        j = 0
        
        i = len(part)
        
        while i <= len(s):
        
            if s[j:i] == part:
            
                s = s[:j] + s[i:]
                
                j = -1
                
                i = len(part) - 1
                
            j += 1
            
            i += 1
            
        return s
        

Complexity Analysis:

Time Complexity: O(N * M), where N is the length of s and M is the length of part. In the worst case, we iterate multiple times to remove part from s.

Space Complexity: O(1), as we modify s in place without additional data structures.
