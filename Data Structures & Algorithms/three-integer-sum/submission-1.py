class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        
        [-1,0,1,2,-1,-4]

        -4, -1, -1, 0, 1, 2
        """
        sorted_arr = sorted(nums)


        i = 0
        n = len(nums)

        triplets_set = set()
        #-2,0,1,1,2
        while i < len(nums)-2: #1
            j = i + 1 #2
            k = n-1 #5

            while j < k:
                if sorted_arr[i] + sorted_arr[j] + sorted_arr[k] > 0:
                    k -=1
                    continue
                elif sorted_arr[i] + sorted_arr[j] + sorted_arr[k] < 0:
                    j +=1
                    continue

                if sorted_arr[i] + sorted_arr[j] + sorted_arr[k] == 0:
                    triplets_set.add((sorted_arr[i], sorted_arr[j], sorted_arr[k]))
                    k -=1
                    j +=1
            i +=1


        return list(list(triplet) for triplet in triplets_set)



