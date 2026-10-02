class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        longest = 0

        left, right= 0,1

        theset = set()
        theset.add(s[left])
        while right < len(s):

            if s[right] not in theset:
                theset.add(s[right])
                longest = max(longest, right - left + 1)
                right += 1
            else:
                while s[right] in theset:
                    theset.remove(s[left])
                    left +=1

                theset.add(s[right])
                right +=1
            
            
        longest = max(longest, right - left)
            
        return longest
                
