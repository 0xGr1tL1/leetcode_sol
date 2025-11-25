class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        s = {}
        for c in magazine:
            s[c] = s.get(c, 0) + 1   
        
        for c in ransomNote:
            if s.get(c, 0) == 0:
                return False
            s[c] -= 1
        
        return True
        
    
