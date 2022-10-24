"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""

def solution(s: str) -> bool:
    from collections import deque
    stack = deque([])
    for i in s:
        if i in '({[':
            stack.append(i)

        elif i == ')' and len(stack) != 0 and stack[-1] == '(':
            stack.pop()
        
        elif i == '}' and len(stack) != 0 and stack[-1] == '{':
            stack.pop()
        
        elif i == ']' and len(stack) != 0 and stack[-1] == '[':
            stack.pop()

        else:
            return False

    return len(stack) == 0



if __name__ == '__main__':
    print(solution("{()()()()()()}"))


