class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)

        setNums = set(nums)
        res = 1
        for num in setNums:
            if num-1 not in setNums:
                curr = num
                count = 1
                while curr+1 in setNums:
                    curr+=1
                    count +=1
                res = max(count,res)
        return res

