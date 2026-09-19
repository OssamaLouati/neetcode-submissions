class Solution:


    """
        {2,20,4,10,3,4,5}


    """
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 1
        
        if len(nums) == 0:
            return 0

        max_conseq = 1
        nums_set = set(nums)

        mmap = {}
        
        for num in nums:
            conseq = 1
            if (num - 1) in nums_set:
                i = num - 1
                while i in nums_set:
                    if i in mmap:
                        conseq += mmap[i]
                        break
                    conseq += 1
                    i -= 1
                max_conseq = max(max_conseq, conseq)
                mmap[num] = conseq
        return max_conseq


