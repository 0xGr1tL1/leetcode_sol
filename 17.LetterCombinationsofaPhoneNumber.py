class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits_map = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl",
                      '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        
        def process(idx,cmb):
            if idx == len(digits):
                res.append(cmb[:])
                return 
            for letter in digits_map[digits[idx]]:
                process(idx + 1,cmb + letter)
            
        
        res = []
        process(0,"")
        return res
        
        
        