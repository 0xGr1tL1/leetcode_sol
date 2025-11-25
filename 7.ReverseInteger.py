class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tmp = abs(x)
        res = 0
        while tmp :
            digit = tmp%10
            res = res*10 + digit
            tmp = tmp//10
            
            if res > 2**31-1 or res <-(2**31):
                return 0
        if x<0:
            return -res
        return res

