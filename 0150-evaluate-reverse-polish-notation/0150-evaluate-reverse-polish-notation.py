class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        int_stack = []
        operators = ['+','-','*', '/']
        for token in tokens:
            numbers_count = len(int_stack)
            if token in operators and numbers_count >= 2:
                num2 = int_stack.pop()
                num1 = int_stack.pop()

            if token == '+':
                int_stack.append(num1 + num2)

            elif token == '-':
                if num2 < 0:
                    int_stack.append(num1 + abs(num2))
                else:
                    int_stack.append(num1 - num2)

            elif token == '*':
                if num1 < 0 and num2 < 0:
                    int_stack.append(abs(num1) * abs(num2))
                else:
                    int_stack.append(num1 * num2)

            elif token == '/':

                if num1 < 0 and num2 < 0:
                    int_stack.append(abs(num1) // abs(num2))
                elif num1 < 0 or num2 < 0:
                    int_stack.append(abs(num1) // abs(num2) * -1)
                else:
                    int_stack.append(num1 // num2)

            else:
                int_stack.append(int(token))

        result = int_stack[0]
        return result