class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                num = int(token)
                stack.append(num)
                print("num",token, stack)
            else:
                first_num = stack.pop()
                second_num = stack.pop()
                if token == "+":
                    stack.append(first_num + second_num)
                elif token == "-":
                    stack.append(second_num - first_num)
                elif token == "*":
                    stack.append(first_num * second_num)
                else:
                    stack.append(int(second_num / first_num))
                print(token, stack)
            
        return stack[0]