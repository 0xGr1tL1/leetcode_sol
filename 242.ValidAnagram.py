class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        letters = {}
        
        for letter in s:
            letters[letter] = letters.get(letter,0) + 1 
        
        for letter in t :
            if letter in letters :
                if not letters[letter]:
                    return False
                letters[letter] -= 1
            else :
                return False
        return True
    
                    