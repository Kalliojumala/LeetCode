"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Constraints:

    0 <= s.length <= 3 * 104
    s[i] is '(', or ')'.
"""

def solution_slow(s):
    count = 0 
    stack = []
    curr = 0
    distances = [0]
    
    for i in s:
        if i == '(':
            stack.append((i, curr))
            

        elif i == ')':
            if len(stack) != 0 and stack[-1][0] == '(':
                curr += 2
                stack.pop()
                count = max(count, curr)
            else:
                distances.append(curr)
                curr = 0
        
    count = max(count, curr)

    if len(stack) == 0:
         return count

    stack.append(('(', curr))
    max_stack_distance = stack[0][1]

    for i in range(len(stack)-1):
        max_stack_distance = max(max_stack_distance, abs(stack[i][1] - stack[i+1][1]))

    return max(max_stack_distance, max(distances))


def solution(s):
    count = 0 
    stack = []
    curr = 0
    distances = [0]
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append((s[i], i))
            

        elif s[i] == ')':
            if len(stack) != 0 and stack[-1][0] == '(':
                curr += 2
                stack.pop()
                count = max(count, curr)
            else:
                distances.append(curr)
                curr = 0
        
    count = max(count, curr)
    print(stack, distances, curr)
    if len(stack) == 0:
         return count

if __name__ == '__main__':
    s = "((())"
    print(solution(s))
