class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        
        -100 -50 10 0.  t = -150
        
        """

        i, j = 0, len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                break

            if  numbers[i] + numbers[j] > target:
                j -=1

            if  numbers[i] + numbers[j] < target:
                i +=1
        
        return [i+1, j+1]

               