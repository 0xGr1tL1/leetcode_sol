class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
       
        if dividend == 0:
            return 0
        
        
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
       
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
       
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
       
        while dividend >= divisor:
            temp_divisor = divisor 
            multiple = 1           
            
            
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1  # << 1 is just  *2
                multiple <<= 1      
            
        
            dividend -= temp_divisor
            quotient += multiple
            
           
        return quotient * sign