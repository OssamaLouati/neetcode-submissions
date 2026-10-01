class Solution:
    def trap(self, height: List[int]) -> int:   
        maxLeft = []
        maxRight = []


        left_so_far = 0
        right_so_far = 0

        for h in height:
            if h > left_so_far:
                maxLeft.append(h)
                left_so_far = h
            else:
                maxLeft.append(left_so_far)

        right_so_far = 0
        for h in height[::-1]:
            if h > right_so_far:
                right_so_far = h
                maxRight.append(right_so_far)
                
            else:
                maxRight.append(right_so_far)

        maxRight.reverse()


        result = 0

        for i, h in enumerate(height):

            trapped = min(maxLeft[i], maxRight[i]) - h

            if trapped>0:
                result += trapped

        return result
        
        