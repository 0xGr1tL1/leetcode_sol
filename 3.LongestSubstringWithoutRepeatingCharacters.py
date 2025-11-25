class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)

        seen = set()
        left = 0
        right = 0
        output = 0

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                output = max(output, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1

        return output
