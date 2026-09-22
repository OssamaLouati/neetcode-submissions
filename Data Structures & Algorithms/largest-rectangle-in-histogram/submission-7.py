class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            if stack:
                if height == stack[-1][1]:
                    continue

                index = i

                while stack and height < stack[-1][1]:
                    max_area = max(max_area,stack[-1][1] * (i - stack[-1][0]))
                    index = stack[-1][0]
                    stack.pop()
                stack.append((index, height))
            else:
                stack.append((i, height))

                
        print(stack)
        while stack:
            max_area = max(max_area, (n - stack[-1][0]) * stack[-1][1])
            stack.pop()

        return max_area


                

