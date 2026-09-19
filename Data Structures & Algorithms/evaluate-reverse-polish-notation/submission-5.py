class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case "+":
                    second = stack.pop()
                    first = stack.pop()
                    res = int(second) + int(first)
                    stack.append(res)
                case "-":
                    second = stack.pop()
                    first = stack.pop()
                    res = int(first) - int(second)
                    stack.append(res)
                case "*":
                    second = stack.pop()
                    first = stack.pop()
                    res = int(first) * int(second)
                    stack.append(res)
                case "/":
                    second = stack.pop()
                    first = stack.pop()
                    if int(second) == 0:
                        raise ZeroDivisionError("division by zero in RPN expression")
                    res = int(first) / int(second)
                    stack.append(int(res))
                case _:
                    stack.append(int(token))

        return stack.pop()
