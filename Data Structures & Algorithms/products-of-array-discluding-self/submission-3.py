class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_so_far = []
        temp = 1
        for num in nums:
            temp = temp * num
            left_so_far.append(temp)

        right_so_far = [1] * len(nums)
        temp = 1

        for i in range(len(nums)-1, -1, -1):
            temp = temp * nums[i]
            right_so_far[i] = temp

        res = []
        for i in range(len(nums)):
            l_idx = i - 1
            r_idx = i + 1
            if l_idx < 0:
                l = 1
            else:
                l = left_so_far[l_idx]
            if r_idx >= len(right_so_far):
                r = 1
            else:
                r = right_so_far[r_idx]
            
            res.append(l * r)

        return res



        # 1, 2,  8, 48
        #48, 48, 24, 6
        #
        