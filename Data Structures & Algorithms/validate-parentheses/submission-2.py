class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            match c:
                case '(':
                    stack.append('(')
                case ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                case '[':
                    stack.append('[')
                case ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                case '{':
                    stack.append('{')
                case '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        return True if not stack else False
                
        