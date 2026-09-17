class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        unique_elems = list(freq_map.keys())

        unique_elems.sort(key=lambda x: freq_map[x], reverse=True)

        res = []
        for i in range(k):
            res.append(unique_elems[i])

        return res