class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        heap = []

        for num, freq in freq_map.items():
            heapq.heappush(heap, (-freq, num))

        res = []

        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
    
        return res