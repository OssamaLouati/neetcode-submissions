class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, x in enumerate(nums):
            diff = target - x

            if diff in map:
                return [map.get(diff), i]

            map[x] = i

        return None
