#Given a string s, find the length of the longest substring without repeating characters.
import time 

def solution(s: str):
    from collections import deque

    longest = 0
    stack = deque([])
    
    for i in range(len(s)):
        if s[i] not in stack:
            stack.append(s[i])
        else:
            longest = max(longest, len(stack))
            for _ in range(i):
                if stack[0] == s[i]:
                    stack.popleft()
                    stack.append(s[i])
                    break
                stack.popleft()

    return max(longest, len(stack)) #int, len of longest sub str 

def solution_o2(s):
    count = 0 
    for i in range(len(s)):
        hash_table = {}
       
        for j in range(i, len(s)):
            if s[j] not in hash_table:
                hash_table[s[j]] = 1
            else:
                break
        count = max(count, len(hash_table))
            
    return count

s = "pwazxbacdfgh" * 10**6 # expected 11

sol1_start = time.time()
print(solution(s))
sol1_end = time.time()
print(f"Function took {sol1_end-sol1_start} seconds.")

sol2_start = time.time()
print(solution_o2(s))
sol2_end = time.time()
print(f"Function took {sol2_end-sol2_start} seconds.")

