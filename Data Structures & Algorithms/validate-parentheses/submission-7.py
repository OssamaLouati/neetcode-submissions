class Solution:
    def isValid(self, s: str) -> bool:
        openers = {"(", "[", "{"}
        closers = {"}", "]", ")"}
        m = {
            ")": "(",
            "]":"[",
            "}":"{"
            }
        stack = []
        
        for c in s:
            if c in m:
                if len(stack) == 0:
                    return False
                if m[c] != stack[-1]:
                    return False
                stack.pop()
            
            if c in m.values():
                stack.append(c)

        return len(stack) == 0
            
         