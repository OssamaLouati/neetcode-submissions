class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)

        res = [0] * n

        stack = []


        for i, temp in enumerate(temperatures):
            if stack:
                while stack and temp > stack[-1][1]:
                        days = i - stack[-1][0]
                        res[stack[-1][0]] = days
                        stack.pop()
                stack.append((i, temp))
            else:
                stack.append((i, temp))

        return res



        