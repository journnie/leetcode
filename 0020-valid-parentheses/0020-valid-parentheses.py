class Solution:
    def isValid(self, s: str) -> bool:
        bracket_sets = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            # opening bracket
            if ch in bracket_sets.values():
                stack.append(ch)
                
            # closing bracket
            else:
                if not stack or bracket_sets[ch] not in stack[-1]:
                    return False
                stack.pop()
        if stack:
            return False
        return True