class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []
        for i in range(len(operations)):
            ch = operations[i]

            if ch == '+':
                if len(score_stack) < 2:
                    continue
                score_stack.append(score_stack[-1] + score_stack[-2])


            elif ch == 'D':
                if len(score_stack) < 1:
                    continue
                score = score_stack[-1]*2
                score_stack.append(score)

            elif ch == 'C':
                if len(score_stack) < 1:
                    continue
                score_stack.pop()

            else:
                score = int(ch)
                score_stack.append(score)

        if score_stack:
            result = sum(score_stack)
        else:
            result = 0


        return result